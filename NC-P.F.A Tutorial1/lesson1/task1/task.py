

def get_next_tab_pos(cur_pos, TAB_WIDTH):
    if cur_pos % TAB_WIDTH == 0:
        return cur_pos + TAB_WIDTH + 1
    else:
        return 3
