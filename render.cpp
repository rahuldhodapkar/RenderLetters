/** render.c
 * core file to individually render all glyphs in an arbitrary character
 * system. 
 */

#include <boost/utility/binary.hpp>
#include <stdio.h>
#include <pango/pangocairo.h>
#include <string.h>
#include "consts.h"

void rendertext(cairo_t *cr, char* data) {
	PangoLayout *layout;
	PangoFontDescription *desc;

	cairo_translate(cr, 10, 20);
	layout = pango_cairo_create_layout(cr);

    pango_layout_set_text(layout, data, -1);
	desc = pango_font_description_from_string("Sans Bold 12");
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

void buildchar(char **cs, unsigned long long data) { 
    printf("trying to build charater\n");
    unsigned char mnmask = BOOST_BINARY(   111111 );
    unsigned char mnpre  = BOOST_BINARY( 10000000 );

    int nSeq = 0; 
    unsigned char capMask = 0;
    unsigned char capPre = 0;

    if (data < (1 << 8)) {
        printf("captured on 1 byte seq\n");
        // 1 byte seq.
        capMask = BOOST_BINARY(  1111111 );
        capPre  = BOOST_BINARY(        0 );
        nSeq = 0;
    }
    else if (data < (1 << 12)) {
        printf("captured on 2 byte seq\n");
        // 2 byte seq.
        capMask = BOOST_BINARY(    11111 );
        capPre  = BOOST_BINARY( 11000000 );

        nSeq = 1;
    }
    else if (data < (1 << 17)) {
        printf("captured on 3 byte seq\n");
        // 3 byte seq.
        capMask = BOOST_BINARY(     1111 );
        capPre  = BOOST_BINARY( 11100000 );

        nSeq = 2;
    }
    else if (data < (1 << 22)) { 
        printf("captured on 4 byte seq\n");
        // 4 byte seq.
        capMask = BOOST_BINARY(      111 );
        capPre  = BOOST_BINARY( 11110000 );

        nSeq = 3;
    }
    else {
        printf("unencodable number passed\n");
    }

    (*cs)[nSeq + 1] = '\0';   // null terminate C string

    unsigned char val;
    for (int i = nSeq; i > 0; i--) { 
        val = data & mnmask;
        val = val + mnpre;
        (*cs)[nSeq + i] = val;
        
        printf("writing %x at %d\n", val, i);

        data = data >> 6;
    }

    val = data & capMask;
    val = val + capPre;

    printf("writing %x at 0\n", val);

    (*cs)[0] = val;
}

int main(int argv, char** argc) {

    char *name = new char[5];
    char *loc = new char[6];

    strcpy(loc, "a.png");

    unsigned long long glyphData = 0x019c; 

    printf("glyph is : %llx\n", glyphData);

    buildchar(&name, glyphData);
    strcpy(name, "Ɯ");

    for(int i = 0; i < strlen(name); i++) { 
        printf("%x ", (unsigned char) name[i]);
    }
    printf("\n");

    generateglyph(name, loc);

    delete name;
    delete loc;
}
