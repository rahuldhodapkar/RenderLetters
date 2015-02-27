
CC=gcc
CFLAGS=-Wall 
INCLUSIONS=-D_REENTRANT -I/opt/X11/include/cairo -I/opt/X11/include/pixman-1 -I/opt/X11/include -I/opt/X11/include/freetype2 -I/opt/X11/include/libpng15 -I/opt/X11/include -I/usr/local/Cellar/pango/1.36.8/include/pango-1.0 -I/usr/local/Cellar/glib/2.42.0/include/glib-2.0 -I/usr/local/Cellar/glib/2.42.0/lib/glib-2.0/include -I/usr/local/opt/gettext/include -L/opt/X11/lib -L/usr/local/Cellar/pango/1.36.8/lib -L/usr/local/Cellar/glib/2.42.0/lib -L/usr/local/opt/gettext/lib -lpangocairo-1.0 -lpango-1.0 -lgobject-2.0 -lglib-2.0 -lintl -lcairo 

render: render.c
	$(CC) $(CFLAGS) $(INCLUSIONS) $^ -o render
	
