
CC=clang++
CFLAGS=-Wall 

# $(pkg-config --cflags --libs pangocairo)
INCLUSIONS=-D_REENTRANT -I/usr/local/Cellar/pango/1.36.8/include/pango-1.0 -I/usr/local/Cellar/cairo/1.14.0/include/cairo -I/usr/local/Cellar/glib/2.42.0/include/glib-2.0 -I/usr/local/Cellar/glib/2.42.0/lib/glib-2.0/include -I/usr/local/opt/gettext/include -I/usr/local/Cellar/pixman/0.32.6/include/pixman-1 -I/usr/local/Cellar/fontconfig/2.11.1/include -I/usr/local/Cellar/freetype/2.5.3_1/include/freetype2 -I/usr/local/Cellar/libpng/1.6.13/include/libpng16 -I/opt/X11/include -L/usr/local/Cellar/pango/1.36.8/lib -L/usr/local/Cellar/glib/2.42.0/lib -L/usr/local/opt/gettext/lib -L/usr/local/Cellar/cairo/1.14.0/lib -lpangocairo-1.0 -lpango-1.0 -lgobject-2.0 -lglib-2.0 -lintl -lcairo 

render: render.cpp
	$(CC) $(CFLAGS) $(INCLUSIONS) $^ -o render
	
