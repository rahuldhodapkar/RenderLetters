/** render.c
 * core file to individually render all glyphs in an arbitrary character
 * system. 
 */

#include <boost/utility/binary.hpp>
#include <stdio.h>
#include <pango/pangocairo.h>
#include <string.h>
#include "consts.h"
#include <sstream>
#include <iostream>
#include <cstring>
#include <string>

static void
list_fonts ()
{
    int i;
    PangoFontFamily ** families;
    int n_families;
    PangoFontMap * fontmap;

    fontmap = pango_cairo_font_map_get_default();
    pango_font_map_list_families (fontmap, & families, & n_families);
    printf ("There are %d families\n", n_families);
    for (i = 0; i < n_families; i++) {
        PangoFontFamily * family = families[i];
        const char * family_name;

        family_name = pango_font_family_get_name (family);
        printf ("Family %d: %s\n", i, family_name);
    }
    g_free (families);
}

void rendertext(cairo_t *cr, char* data) {
	PangoLayout *layout;
	PangoFontDescription *desc;

	cairo_translate(cr, 10, 10);
	layout = pango_cairo_create_layout(cr);

    pango_layout_set_text(layout, data, -1);
	desc = pango_font_description_from_string(FONT_STYLE_AND_SIZE);
    pango_layout_set_font_description(layout, desc);
	pango_font_description_free(desc);
    
    cairo_set_source_rgb(cr, 0.0, 0.0, 0.0);
	pango_cairo_update_layout(cr, layout);
	pango_cairo_show_layout(cr, layout);

	g_object_unref(layout);
}

void generateglyph(char* glyph, char* filename) {
    cairo_t *cr;
    cairo_status_t status;
    cairo_surface_t *surface;

	surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 
                                         GLYPH_SIZE, GLYPH_SIZE);
	cr = cairo_create(surface);

	cairo_set_source_rgb(cr, 1.0, 1.0, 1.0);
	cairo_paint(cr);

    rendertext(cr, glyph);

    cairo_destroy(cr);
	status = cairo_surface_write_to_png(surface, filename);
	cairo_surface_destroy(surface);
}

char *buildchar(unsigned long long data) { 
    char *cs = new char[6];
    
    unsigned char mnmask = BOOST_BINARY(   111111 );
    unsigned char mnpre  = BOOST_BINARY( 10000000 );

    int nSeq = 0; 
    unsigned char capMask = 0;
    unsigned char capPre = 0;

    if (data < (1 << 7)) {
        // printf("captured on 1 byte seq\n");
        // 1 byte seq.
        capMask = BOOST_BINARY(  1111111 );
        capPre  = BOOST_BINARY(        0 );
        nSeq = 0;
    }
    else if (data < (1 << 11)) {
        // printf("captured on 2 byte seq\n");
        // 2 byte seq.
        capMask = BOOST_BINARY(    11111 );
        capPre  = BOOST_BINARY( 11000000 );

        nSeq = 1;
    }
    else if (data < (1 << 16)) {
        // printf("captured on 3 byte seq\n");
        // 3 byte seq.
        capMask = BOOST_BINARY(     1111 );
        capPre  = BOOST_BINARY( 11100000 );

        nSeq = 2;
    }
    else if (data < (1 << 21)) { 
        // printf("captured on 4 byte seq\n");
        // 4 byte seq.
        capMask = BOOST_BINARY(      111 );
        capPre  = BOOST_BINARY( 11110000 );

        nSeq = 3;
    }
    else {
        printf("unencodable number passed\n");
    }

    // printf("writing string terminator at %d\n", nSeq + 1);
    cs[nSeq + 1] = '\0';   // null terminate C string

    unsigned char val;
    for (int i = nSeq; i > 0; i--) { 
        val = data & mnmask;
        val = val + mnpre;
        cs[i] = val;
        
        // printf("writing %x at %d\n", val, i);

        data = data >> 6;
    }

    val = data & capMask;
    val = val + capPre;

    // printf("writing %x at 0\n", val);

    cs[0] = val;

    return cs;
}

int main(int argv, char** argc) {
    char *name;
    char *loc = new char[200];

    for (unsigned long long glyphData = 0xA980; glyphData <= 0xA9DF; glyphData++) {
        name = buildchar(glyphData);
        printf("%s\n", name);

        std::stringstream stringStream;
        stringStream << "letterSet/" << name << ".png";
        strcpy(loc, stringStream.str().c_str());

        generateglyph(name, loc);
        delete name;
    }
    delete loc;
    list_fonts();
}