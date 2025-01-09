import drawsvg as draw

# thickness of material 
T = 3.0;
kerf = 0.1;

cut_color = 'black'
label_color = 'blue'
layout_color = 'red'

labels = True;
save_png = True;
box_joints = True;

# additional space to add to the inner box
# "average" matchbox car is 3inx1inx1in
add_width  = 74.0;
add_height = 24.0;
add_depth  = 18.0;

# finger joint dimensions
#     |------|
#  T  |      |
#  ---|      |---
#   T   T  T   T
#  gap/2 wid  gap/2
# <-- interval-->
#
tab_width = 2.0 * T;
tab_gap   = T + T;
tab_interval = tab_width + tab_gap;

#
# dimension below are derived from the Homemade Puzzles
# "The Matchbox T-plans" PDF
#

box_base_width  =  10.0 * T + add_width;
box_base_height =   8.0 * T + add_height;
box_base_thick  = T;

box_side_height =  8.0 * T + add_height;
box_side_width  =  3.0 * T + add_depth;
box_side_thick  = T;

top_rail_width  = 11.0 * T + add_width;
top_rail_height =  1.0 * T;

side_rail_width  = 6.0 * T + add_depth;
side_rail_height = 1.0 * T;

back_width  = 16.0*T + add_width;
back_height = 10.0*T + add_depth;

front_width  = back_width;
front_height = back_height;

# origin of left side rail on back piece
back_left_x  =       T;
back_left_y  = 3.0 * T;


# origin of right side rail on back piece
back_right_x =  back_width - 2.0*T;
back_right_y = T;

# origin of top rail on back piece
back_top_x  = 2.0 * T;
back_top_y  =       T;

# origin of bottom rail on back piece
back_bottom_x  = 3.0 * T;
back_bottom_y  = back_height - 2.0 * T;

# origin of box left side on back piece
back_box_left_x = 3.0*T;
back_box_left_y = 3.0*T;

# origin of box right side on back piece
back_box_right_x = back_width - 4.0*T;
back_box_right_y = 3.0*T;

# origin of box base on back piece
back_box_base_x = 3.0*T;
back_box_base_y = front_height - 4.0*T;

# origin of box base on front piece
front_width  = back_width;
front_height = back_height;

# origin of left side rail on front piece
front_left_x  = T;
front_left_y  = T;


# origin of right side rail on front piece
front_right_x =  front_width - 2.0*T;
front_right_y = 3.0*T;

# origin of top rail on front piece
front_top_x  = 3.0 * T;
front_top_y  =       T;

# origin of bottom rail on front piece
front_bottom_x  = 2.0 * T;
front_bottom_y  = front_height - 2.0 * T;

# origin of box left side on front piece
front_box_left_x = 3.0*T;
front_box_left_y = 3.0*T;

# origin of box right side on front piece
front_box_right_x = front_width - 4.0*T;
front_box_right_y = 3.0*T;

# origin of box base on front piece
front_box_base_x = 3.0*T;
front_box_base_y = front_height - 4.0*T;

left_holder_width  = 8.0 * T + add_height;
left_holder_height = 5.0 * T + add_depth;

left_runner_width  = 6.0 * T + add_height;
left_runner_height = 7.0 * T + add_depth;

left_outer_width  =  8.0 * T + add_height;
left_outer_height = 10.0 * T + add_depth;

right_holder_width  = 8.0 * T + add_height;
right_holder_height = 5.0 * T + add_depth;

right_runner_width  = 6.0 * T + add_height;
right_runner_height = 7.0 * T + add_depth;

right_outer_width  =  8.0 * T + add_height;
right_outer_height =  9.0 * T + add_depth;

top_holder_width  = 11.0 * T + add_width;
top_holder_height =  8.0 * T + add_height;

top_runner_width  = 13.0 * T + add_width;
top_runner_height =  6.0 * T + add_height;

top_outer_width  = 15.0 * T + add_width;
top_outer_height =  8.0 * T + add_height;

bottom_holder_width  = 10.0 * T + add_width;
bottom_holder_height =  8.0 * T + add_height;

bottom_runner_width  = 12.0 * T + add_width;
bottom_runner_height =  6.0 * T + add_height;

bottom_outer_width  = 14.0 * T + add_width;
bottom_outer_height =  8.0 * T + add_height;


def finger_box( x=0, y=0,
                width = 100, height=50, box_id="DEFAULT", labels=False, label="Default",
                left_in = False, left_out=False,
                bottom_in=False, bottom_out=False,
                right_in=False, right_out=False,
                top_in=False, top_out=False):
    
    g = draw.Group(id=box_id, fill='none', stroke=cut_color, stroke_width = 0.1);

    x_tabs = int(width)  // int(tab_interval) - 1;
    y_tabs = int(height) // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    y_margin = (height- y_tabs * tab_interval ) / 2.0;
        
    # path origin
    p = draw.Path();
    p.M(x-kerf,y-kerf);

    if left_in:
        # down left side with in-pockets
        p.L( x-kerf, y + y_margin - kerf );
        for y2 in range( y_tabs ):
            p.V(               y + y_margin +     y2*tab_interval + (tab_gap/2.0) + kerf );
            p.H( x + T - kerf );
            p.V(               y + y_margin + (y2+1)*tab_interval - (tab_gap/2.0) - kerf );
            p.H( x-kerf        );
    elif left_out:
        # down left side with out-tabs
        p.L( x-kerf, y + y_margin - kerf );
        for y2 in range( y_tabs ):
            p.V(               y + y_margin +     y2*tab_interval + (tab_gap/2.0) - kerf );
            p.H( x - T - kerf );
            p.V(               y + y_margin + (y2+1)*tab_interval - (tab_gap/2.0) + kerf );
            p.H( x      - kerf );
    p.L( x-kerf, y+height+kerf );

    if bottom_out:
        # across bottom with out-tabs
        p.L( x + x_margin - kerf, y + height + kerf);
        for x2 in range( x_tabs):
            p.H( x + x_margin +     x2*tab_interval + (tab_gap/2.0) - kerf);
            p.V( y + height + T + kerf );
            p.H( x + x_margin + (x2+1)*tab_interval - (tab_gap/2.0) + kerf);
            p.V( y + height + kerf );
    elif bottom_in:
        raise ValueError;
    p.L( x + width + kerf, y + height + kerf);

    if right_in:
        # up right side with in-pockets
        p.L( x + width + kerf, y + height - y_margin - kerf );
        for y2 in range( y_tabs):
            p.V( y + height - y_margin -     y2*tab_interval - (tab_gap/2.0) - kerf);
            p.H( x + width - T + kerf);
            p.V( y + height - y_margin - (y2+1)*tab_interval + (tab_gap/2.0) + kerf);
            p.H( x + width + kerf );
    elif right_out:
        raise ValueError;
    p.L( x + width + kerf, y - kerf);

    if top_out:
        # across top with out-tabs
        p.L( x + width - x_margin + kerf , y - kerf );
        for x2 in range( x_tabs):
            p.H( x + width - x_margin -    x2*tab_interval - (tab_gap/2.0) + kerf );
            p.V( y - T - kerf );
            p.H( x + width - x_margin - (x2+1)*tab_interval + (tab_gap/2.0) - kerf );
            p.V( y - kerf );
    elif top_in:
        raise ValueError;
    p.L( x - kerf, y - kerf );
    
    p.Z(); # closepath

    # add path to group container
    g.append(p);
    
    if labels:
        g.append(draw.Text(label, font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def box_base( x=0, y=0 ):
    g = finger_box( x=x, y=y, box_id="box_base", labels=True, label="Box Base",
                    width  = box_base_width, height = box_base_height,
                    left_in=True, bottom_out=True, right_in=True, top_out=True);
    return g;

def box_side( x=0, y=0 ):
    g = finger_box( x=x, y=y, box_id="box_side", labels=True, label="Box Side",
                    height = box_side_height, width = box_side_width,
                    left_out=True, bottom_out=True, top_out=True);
    return g;

def top_rail( x=0, y=0 ):
    g = finger_box( x=x, y=y, box_id="top_rail", labels=False,
                    width = top_rail_width, height = top_rail_height,
                    bottom_out=True );
    return g;

def side_rail( x=0, y=0 ):
    g = finger_box( x=x, y=y, box_id="side_rail", labels=False,
                    width = side_rail_width, height = side_rail_height,
                    bottom_out=True );
    return g;

def back( x=0, y=0 ):

    width  = back_width;
    height = back_height;
    
    g = draw.Group(id='back', fill='none', stroke=cut_color, stroke_width = 0.1);

    x_tabs = int(width)  // int(tab_interval) - 1;
    y_tabs = int(height) // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    y_margin = (height- y_tabs * tab_interval ) / 2.0;
        
    # main piece
    g.append(draw.Rectangle( x, y, back_width, back_height, stroke=cut_color));

    # side rail guides
    g.append(draw.Rectangle( x + back_left_x, y + back_left_y, 
                             height = side_rail_width,
                             width  = side_rail_height,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + back_right_x, y + back_right_y, 
                             height = side_rail_width,
                             width  = side_rail_height,
                             stroke=layout_color ) );

    # top and bottom rail guides
    g.append(draw.Rectangle( x + back_top_x, y + back_top_y, 
                             width   = top_rail_width,
                             height  = top_rail_height,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + back_bottom_x, y + back_bottom_y, 
                             width   = top_rail_width,
                             height  = top_rail_height,
                             stroke=layout_color ) );

    # box guides
    g.append(draw.Rectangle( x + back_box_left_x, y + back_box_left_y, 
                             width  = box_side_thick,
                             height = box_side_width,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + back_box_right_x, y + back_box_right_y, 
                             width  = box_side_thick,
                             height = box_side_width,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + back_box_base_x, y + back_box_base_y, 
                             height = box_base_thick,
                             width  = box_base_width,
                             stroke=layout_color ) );
    # box side cutouts
    height = box_side_height;

    y_tabs = int(height) // int(tab_interval) - 1;
    y_margin = (height- y_tabs * tab_interval ) / 2.0;

    # only one tab on these, draw rectangle directly rather than using for loop.  This will probably break on re-sizing the object
    g.append(draw.Rectangle( x + back_box_left_x + kerf, y + back_box_left_y + (y_margin + tab_gap/2.0) + kerf, 
                             width  =         T - 2.0*kerf,
                             height = tab_width - 2.0*kerf,
                             stroke=cut_color ) );
    g.append(draw.Rectangle( x + back_box_right_x + kerf, y + back_box_right_y + (y_margin + tab_gap/2.0) + kerf, 
                             width  =         T - 2.0*kerf,
                             height = tab_width - 2.0*kerf,
                             stroke=cut_color ) );

    # box base cutouts for box joint fingers
    width = box_base_width;

    x_tabs = int(width)  // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    
    for x2 in range( x_tabs):
        g.append(draw.Rectangle( x = x + back_box_base_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + back_box_base_y + kerf,
                                 width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));

    # cutouts for top and bottom rails
    width = top_rail_width;

    x_tabs = int(width)  // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    
    for x2 in range( x_tabs):
        g.append(draw.Rectangle( x = x + back_top_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + back_top_y + kerf, width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));
        g.append(draw.Rectangle( x = x + back_bottom_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + back_bottom_y + kerf, width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));

    # cutouts for side rails
    height = side_rail_width;

    y_tabs = int(height)  // int(tab_interval) - 1;
    y_margin = (height - y_tabs * tab_interval ) / 2.0;
    
    for y2 in range( y_tabs):
        g.append(draw.Rectangle( x = x + back_left_x + kerf,
                                 y = y + back_left_y + y_margin + y2*tab_interval + (tab_gap/2.0) + kerf,
                                 width=T-2.0*kerf, height=tab_width-2*kerf, stroke=cut_color));
        g.append(draw.Rectangle( x = x + back_right_x + kerf,
                                 y = y + back_right_y + y_margin + y2*tab_interval + (tab_gap/2.0) + kerf,
                                 width=T-2.0*kerf, height=tab_width-2*kerf, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("Back", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def front( x=0, y=0 ):

    width  = front_width;
    height = front_height;
    
    g = draw.Group(id='front', fill='none', stroke=cut_color, stroke_width = 0.1);

    x_tabs = int(width)  // int(tab_interval) - 1;
    y_tabs = int(height) // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    y_margin = (height- y_tabs * tab_interval ) / 2.0;
        
    # main piece
    g.append(draw.Rectangle( x, y, front_width, front_height, stroke=cut_color));

    # side rail guides
    g.append(draw.Rectangle( x + front_left_x, y + front_left_y, 
                             height = side_rail_width,
                             width  = side_rail_height,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + front_right_x, y + front_right_y, 
                             height = side_rail_width,
                             width  = side_rail_height,
                             stroke=layout_color ) );

    # top and bottom rail guides
    g.append(draw.Rectangle( x + front_top_x, y + front_top_y, 
                             width   = top_rail_width,
                             height  = top_rail_height,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + front_bottom_x, y + front_bottom_y, 
                             width   = top_rail_width,
                             height  = top_rail_height,
                             stroke=layout_color ) );

    # box guides
    g.append(draw.Rectangle( x + front_box_left_x, y + front_box_left_y, 
                             width  = box_side_thick,
                             height = box_side_width,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + front_box_right_x, y + front_box_right_y, 
                             width  = box_side_thick,
                             height = box_side_width,
                             stroke=layout_color ) );
    g.append(draw.Rectangle( x + front_box_base_x, y + front_box_base_y, 
                             height = box_base_thick,
                             width  = box_base_width,
                             stroke=layout_color ) );
    # box side cutouts
    height = box_side_height;

    y_tabs = int(height) // int(tab_interval) - 1;
    y_margin = (height- y_tabs * tab_interval ) / 2.0;

    # only one tab on these, draw rectangle directly rather than using for loop.  This will probably break on re-sizing the object
    g.append(draw.Rectangle( x + front_box_left_x + kerf, y + front_box_left_y + (y_margin + tab_gap/2.0) + kerf, 
                             width  =         T - 2.0*kerf,
                             height = tab_width - 2.0*kerf,
                             stroke=cut_color ) );
    g.append(draw.Rectangle( x + front_box_right_x + kerf, y + front_box_right_y + (y_margin + tab_gap/2.0) + kerf, 
                             width  =         T - 2.0*kerf,
                             height = tab_width - 2.0*kerf,
                             stroke=cut_color ) );

    # box base cutouts for box joint fingers
    width = box_base_width;

    x_tabs = int(width)  // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    
    for x2 in range( x_tabs):
        g.append(draw.Rectangle( x = x + front_box_base_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + front_box_base_y + kerf,
                                 width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));

    # cutouts for top and bottom rails
    width = top_rail_width;

    x_tabs = int(width)  // int(tab_interval) - 1;
    x_margin = (width - x_tabs * tab_interval ) / 2.0;
    
    for x2 in range( x_tabs):
        g.append(draw.Rectangle( x = x + front_top_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + front_top_y + kerf, width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));
        g.append(draw.Rectangle( x = x + front_bottom_x + x_margin + x2*tab_interval + (tab_gap/2.0) + kerf,
                                 y = y + front_bottom_y + kerf, width=tab_width-2.0*kerf, height=T-2*kerf, stroke=cut_color));

    # cutouts for side rails
    height = side_rail_width;

    y_tabs = int(height)  // int(tab_interval) - 1;
    y_margin = (height - y_tabs * tab_interval ) / 2.0;
    
    for y2 in range( y_tabs):
        g.append(draw.Rectangle( x = x + front_left_x + kerf,
                                 y = y + front_left_y + y_margin + y2*tab_interval + (tab_gap/2.0) + kerf,
                                 width=T-2.0*kerf, height=tab_width-2*kerf, stroke=cut_color));
        g.append(draw.Rectangle( x = x + front_right_x + kerf,
                                 y = y + front_right_y + y_margin + y2*tab_interval + (tab_gap/2.0) + kerf,
                                 width=T-2.0*kerf, height=tab_width-2*kerf, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("Front", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def left_holder( x=0, y=0 ):

    width  = left_holder_width;
    height = left_holder_height;
    
    g = draw.Group(id='left_hold', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("L hold", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def left_runner( x=0, y=0 ):

    width  = left_runner_width;
    height = left_runner_height;
    
    g = draw.Group(id='left_run', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    # construction layout guides
    g.append(draw.Rectangle( x = x-T, y = y+T, width = left_holder_width, height = left_holder_height, stroke=layout_color));

    if labels:
        g.append(draw.Text("L run", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def left_outer( x=0, y=0 ):

    width  = left_outer_width;
    height = left_outer_height;
    
    g = draw.Group(id='left_out', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));

    # construction layout guides
    g.append(draw.Rectangle( x = x+T, y = y+    T, width = left_runner_width, height = left_runner_height, stroke=layout_color));
    g.append(draw.Rectangle( x = x,   y = y+2.0*T, width = left_holder_width, height = left_holder_height, stroke=layout_color));
    
    if labels:
        g.append(draw.Text("L out", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def right_holder( x=0, y=0 ):

    width  = right_holder_width;
    height = right_holder_height;
    
    g = draw.Group(id='right_hold', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("R hold", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def right_runner( x=0, y=0 ):

    width  = right_runner_width;
    height = right_runner_height;
    
    g = draw.Group(id='right_run', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    # construction layout guides
    g.append(draw.Rectangle( x = x-T, y = y+T, width = right_holder_width, height = right_holder_height, stroke=layout_color));

    if labels:
        g.append(draw.Text("R run", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def right_outer( x=0, y=0 ):

    width  = right_outer_width;
    height = right_outer_height;
    
    g = draw.Group(id='right_out', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));

    # construction layout guides
    g.append(draw.Rectangle( x = x+T, y = y+    T, width = right_runner_width, height = right_runner_height, stroke=layout_color));
    g.append(draw.Rectangle( x = x,   y = y+2.0*T, width = right_holder_width, height = right_holder_height, stroke=layout_color));
    
    if labels:
        g.append(draw.Text("R out", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def top_holder( x=0, y=0 ):

    width  = top_holder_width;
    height = top_holder_height;
    
    g = draw.Group(id='top_hold', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("T hold", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def top_runner( x=0, y=0 ):

    width  = top_runner_width;
    height = top_runner_height;
    
    g = draw.Group(id='top_run', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    # construction layout guides
    g.append(draw.Rectangle( x = x+T, y = y-T, width = top_holder_width, height = top_holder_height, stroke=layout_color));

    if labels:
        g.append(draw.Text("T run", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def top_outer( x=0, y=0 ):

    width  = top_outer_width;
    height = top_outer_height;
    
    g = draw.Group(id='top_out', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));

    # construction layout guides
    g.append(draw.Rectangle( x = x+T, y = y+T, width = top_runner_width, height = top_runner_height, stroke=layout_color));
    g.append(draw.Rectangle( x = x+2.0*T, y = y, width = top_holder_width, height = top_holder_height, stroke=layout_color));
    
    if labels:
        g.append(draw.Text("T out", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def bottom_holder( x=0, y=0 ):

    width  = bottom_holder_width;
    height = bottom_holder_height;
    
    g = draw.Group(id='bottom_hold', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    if labels:
        g.append(draw.Text("B hold", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def bottom_runner( x=0, y=0 ):

    width  = bottom_runner_width;
    height = bottom_runner_height;
    
    g = draw.Group(id='bottom_run', fill='none', stroke=cut_color, stroke_width = 0.1);

    g.append(draw.Rectangle( x = x, y = y, width = width, height = height, stroke=cut_color));
    
    # construction layout guides
    g.append(draw.Rectangle( x = x+T, y = y-T, width = bottom_holder_width, height = bottom_holder_height, stroke=layout_color));

    if labels:
        g.append(draw.Text("B run", font_size=3,
                           x=x+width/2.0 - 5.0, y=y+height/2.0,
                           stroke=label_color ))
    return g;

def bottom_outer( x=0, y=0 ):

    width  = bottom_outer_width;
    height = bottom_outer_height;
    
    g = draw.Group(id='bottom_out', fill='none', stroke=cut_color, stroke_width = 0.1);

    # rotate 90 degrees to fit
    g.append(draw.Rectangle( x = y, y = x, width = height, height = width, stroke=cut_color));

    # construction layout guides
    g.append(draw.Rectangle( y = x+T, x = y+T, height = bottom_runner_width, width = bottom_runner_height, stroke=layout_color));
    g.append(draw.Rectangle( y = x+2.0*T, x = y, height = bottom_holder_width, width = bottom_holder_height, stroke=layout_color));
    
    if labels:
        g.append(draw.Text("B out", font_size=3,
                           y=x+width/2.0 - 5.0, x=y+height/2.0,
                           stroke=label_color ))
    return g;


# 12in x 12in sheet == 300mm x 300mm    
d = draw.Drawing(300, 300, origin=(0,0) )

d.append( box_base( 5,5 ) );

d.append( box_side( 115,5 ) );

d.append( box_side( 150,5 ) );

d.append( top_rail( 182,5 ) );
d.append( top_rail( 182,12 ) );
d.append( top_rail( 182,19 ) );
d.append( top_rail( 182,26 ) );

d.append( side_rail( 182,33 ) );
d.append( side_rail( 182,40 ) );
d.append( side_rail( 220,33 ) );
d.append( side_rail( 220,40 ) );

d.append( back(5, 60 ) );
d.append( front(130, 60 ) );

d.append( left_holder( 5, 110 ) );
d.append( left_runner( 60, 110 ) );
d.append( left_outer( 110, 110 ) );

d.append( right_holder( 110, 160 ) );
d.append( right_runner( 60, 150 ) );
d.append( right_outer( 5, 145 ) );

d.append( top_holder( 5, 195 ) );
d.append( top_runner( 115, 197 ) );
d.append( top_outer( 160, 110 ) );

d.append( bottom_holder( 5, 245 ) );
d.append( bottom_runner( 112, 247 ) );
d.append( bottom_outer( 160, 230 ) ); # Note: XY swapped to rotate and fit stock


d.save_svg('dsvg_puzzle.svg')

if save_png:
    d.set_pixel_scale(10)  # Set number of pixels per geometry unit
    #d.set_render_size(400, 200)  # Alternative to set_pixel_scale
    d.save_png('dsvg_puzzle.png')

# Display in Jupyter notebook
d.rasterize()  # Display as PNG
d  # Display as SVG
