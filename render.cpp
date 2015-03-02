/** render.c
 * core file to individually render all glyphs in an arbitrary character
 * system. 
 */

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

void buildchar(char **cs, unsigned long long i) { 
    if (i < (1 << 8)) {
        // 1 byte seq.
        
    }
    else if (i < (1 << 12)) {
        // 2 byte seq.

    }
    else if (i < (1 << 17)) {
        // 3 byte seq.

    }
    else if (i < (1 << 22)) { 
        // 4 byte seq.

    }
    else {
        printf("unencodable number passed\n");
    }
}

int main(int argv, char** argc) {

    char *name = new char[5];
    char *loc = new char[6];

    strcpy(name, "name");
    strcpy(loc, "a.png");

    generateglyph(name, loc);

    delete name;
    delete loc;
}
