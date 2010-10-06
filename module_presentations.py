from header_common import *
from header_presentations import *
from header_mission_templates import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
  ("game_credits",prsntf_read_only,"mesh_load_window",[
      (ti_on_presentation_load,
       [(assign, "$g_presentation_credits_obj_1", -1),
        (assign, "$g_presentation_credits_obj_2", -1),
        (assign, "$g_presentation_credits_obj_3", -1),
        (assign, "$g_presentation_credits_obj_4", -1),
        (assign, "$g_presentation_credits_obj_5", -1),
        (assign, "$g_presentation_credits_obj_6", -1),
        (assign, "$g_presentation_credits_obj_7", -1),
        (assign, "$g_presentation_credits_obj_8", -1),
        (assign, "$g_presentation_credits_obj_9", -1),
        (assign, "$g_presentation_credits_obj_10", -1),
        (assign, "$g_presentation_credits_obj_11", -1),
        (assign, "$g_presentation_credits_obj_12", -1),
        (assign, "$g_presentation_credits_obj_1_alpha", 0),
        (assign, "$g_presentation_credits_obj_2_alpha", 0),
        (assign, "$g_presentation_credits_obj_3_alpha", 0),
        (assign, "$g_presentation_credits_obj_4_alpha", 0),
        (assign, "$g_presentation_credits_obj_5_alpha", 0),
        (assign, "$g_presentation_credits_obj_6_alpha", 0),
        (assign, "$g_presentation_credits_obj_7_alpha", 0),
        (assign, "$g_presentation_credits_obj_8_alpha", 0),
        (assign, "$g_presentation_credits_obj_9_alpha", 0),
        ]),
      (ti_on_presentation_run,
       [
        (store_trigger_param_1, ":cur_time"),
        (set_fixed_point_multiplier, 1000),
        (presentation_set_duration, 1000000),
        (try_begin),
          (this_or_next|key_clicked, key_space),
          (this_or_next|key_clicked, key_enter),
          (this_or_next|key_clicked, key_escape),
          (this_or_next|key_clicked, key_back_space),
          (this_or_next|key_clicked, key_left_mouse_button),
          (key_clicked, key_right_mouse_button),
          (presentation_set_duration, 0),
        (try_end),
        (try_begin),
          (lt, "$g_presentation_credits_obj_1", 0),
          (str_store_string, s1, "str_credits_1"),
          (create_text_overlay, "$g_presentation_credits_obj_1", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_1", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_1", 0),
          (position_set_x, pos1, 1500),
          (position_set_y, pos1, 1500),
          (overlay_set_size, "$g_presentation_credits_obj_1", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_1", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_1", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 2000),
          (eq, "$g_presentation_credits_obj_1_alpha", 0),
          (assign, "$g_presentation_credits_obj_1_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_1", 1000, 0x00),
        (else_try),
          (gt, ":cur_time", 3500),
          (lt, "$g_presentation_credits_obj_2", 0),
          (str_store_string, s1, "str_credits_2"),
          (create_text_overlay, "$g_presentation_credits_obj_2", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_2", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_2", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_2", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_2", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_2", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 5500),
          (eq, "$g_presentation_credits_obj_2_alpha", 0),
          (assign, "$g_presentation_credits_obj_2_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_2", 1000, 0x00),
        (else_try),
          (gt, ":cur_time", 7000),
          (lt, "$g_presentation_credits_obj_3", 0),
          (str_store_string, s1, "str_credits_3"),
          (create_text_overlay, "$g_presentation_credits_obj_3", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_3", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_3", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_3", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_3", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_3", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 9000),
          (eq, "$g_presentation_credits_obj_3_alpha", 0),
          (assign, "$g_presentation_credits_obj_3_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_3", 1000, 0),
        (else_try),
          (gt, ":cur_time", 10500),
          (lt, "$g_presentation_credits_obj_4", 0),
          (str_store_string, s1, "str_credits_4"),
          (create_text_overlay, "$g_presentation_credits_obj_4", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_4", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_4", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_4", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_4", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_4", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 12500),
          (eq, "$g_presentation_credits_obj_4_alpha", 0),
          (assign, "$g_presentation_credits_obj_4_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_4", 1000, 0),
        (else_try),
          (gt, ":cur_time", 14000),
          (lt, "$g_presentation_credits_obj_5", 0),
          (str_store_string, s1, "str_credits_5"),
          (create_text_overlay, "$g_presentation_credits_obj_5", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_5", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_5", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_5", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_5", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_5", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 16000),
          (eq, "$g_presentation_credits_obj_5_alpha", 0),
          (assign, "$g_presentation_credits_obj_5_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_5", 1000, 0),
        (else_try),
          (gt, ":cur_time", 17500),
          (lt, "$g_presentation_credits_obj_6", 0),
          (str_store_string, s1, "str_credits_6"),
          (create_text_overlay, "$g_presentation_credits_obj_6", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_6", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_6", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_6", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_6", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_6", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 19500),
          (eq, "$g_presentation_credits_obj_6_alpha", 0),
          (assign, "$g_presentation_credits_obj_6_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_6", 1000, 0),
        (else_try),
          (gt, ":cur_time", 21000),
          (lt, "$g_presentation_credits_obj_7", 0),
          (str_store_string, s1, "str_credits_7"),
          (create_text_overlay, "$g_presentation_credits_obj_7", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_7", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_7", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_7", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_7", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_7", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 23000),
          (eq, "$g_presentation_credits_obj_7_alpha", 0),
          (assign, "$g_presentation_credits_obj_7_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_7", 1000, 0),
        (else_try),
          (gt, ":cur_time", 24500),
          (lt, "$g_presentation_credits_obj_8", 0),
          (str_store_string, s1, "str_credits_8"),
          (create_text_overlay, "$g_presentation_credits_obj_8", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_8", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_8", 0),
          (position_set_x, pos1, 1750),
          (position_set_y, pos1, 1750),
          (overlay_set_size, "$g_presentation_credits_obj_8", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 375),
          (overlay_set_position, "$g_presentation_credits_obj_8", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_8", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 26500),
          (eq, "$g_presentation_credits_obj_8_alpha", 0),
          (assign, "$g_presentation_credits_obj_8_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_8", 1000, 0),
        (else_try),
          (gt, ":cur_time", 28000),
          (lt, "$g_presentation_credits_obj_9", 0),
          (str_store_string, s1, "str_credits_10"),
          (create_text_overlay, "$g_presentation_credits_obj_9", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_9", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_9", 0),
          (position_set_x, pos1, 750),
          (position_set_y, pos1, 750),
          (overlay_set_size, "$g_presentation_credits_obj_9", pos1),
          (position_set_x, pos1, 250),
          (position_set_y, pos1, 485),
          (overlay_set_position, "$g_presentation_credits_obj_9", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_9", 1000, 0xFF),

          (str_store_string, s1, "str_credits_11"),
          (create_text_overlay, "$g_presentation_credits_obj_10", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_10", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_10", 0),
          (position_set_x, pos1, 750),
          (position_set_y, pos1, 750),
          (overlay_set_size, "$g_presentation_credits_obj_10", pos1),
          (position_set_x, pos1, 750),
          (position_set_y, pos1, 470),
          (overlay_set_position, "$g_presentation_credits_obj_10", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_10", 1000, 0xFF),

          (str_store_string, s1, "str_credits_12"),
          (create_text_overlay, "$g_presentation_credits_obj_11", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
          (overlay_set_color, "$g_presentation_credits_obj_11", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_11", 0),
          (position_set_x, pos1, 750),
          (position_set_y, pos1, 750),
          (overlay_set_size, "$g_presentation_credits_obj_11", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 105),
          (overlay_set_position, "$g_presentation_credits_obj_11", pos1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_11", 1000, 0xFF),
        (else_try),
          (gt, ":cur_time", 34000),
          (eq, "$g_presentation_credits_obj_9_alpha", 0),
          (assign, "$g_presentation_credits_obj_9_alpha", 1),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_9", 1000, 0),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_10", 1000, 0),
          (overlay_animate_to_alpha, "$g_presentation_credits_obj_11", 1000, 0),
        (else_try),
          (gt, ":cur_time", 35500),
          (lt, "$g_presentation_credits_obj_12", 0),
          (str_store_string, s1, "str_credits_9"),
          (create_text_overlay, "$g_presentation_credits_obj_12", s1, tf_center_justify|tf_double_space),
          (overlay_set_color, "$g_presentation_credits_obj_12", 0),
          (overlay_set_alpha, "$g_presentation_credits_obj_12", 0xFF),
          (position_set_x, pos1, 1000),
          (position_set_y, pos1, 1000),
          (overlay_set_size, "$g_presentation_credits_obj_12", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, -4800),
          (overlay_set_position, "$g_presentation_credits_obj_12", pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, 760),
          (overlay_animate_to_position, "$g_presentation_credits_obj_12", 70000, pos1),
        (else_try),
          (gt, ":cur_time", 105500),
          (presentation_set_duration, 0),
        (try_end),
        ]),
      ]),

  ("game_profile_banner_selection", 0, "mesh_load_window", [
    (ti_on_presentation_load, [
      (set_fixed_point_multiplier, 1000),
      (str_store_string, s1, "str_profile_banner_selection_text"),
      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg1, pos1),
      (overlay_set_text, reg1, s1),
      (create_button_overlay, "$g_presentation_obj_profile_banner_selection_1", "@Next Page", tf_center_justify),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 50),
      (overlay_set_position, "$g_presentation_obj_profile_banner_selection_1", pos1),

      (create_button_overlay, "$g_presentation_obj_profile_banner_selection_2", "str_use_default_banner", tf_center_justify),
      (position_set_x, pos1, 300),
      (position_set_y, pos1, 50),
      (overlay_set_position, "$g_presentation_obj_profile_banner_selection_2", pos1),

      (assign, ":x_pos", 150),
      (assign, ":y_pos", 575),
      (store_mul, ":starting_banner", 16, "$g_presentation_page_no"),
      (store_add, ":ending_banner", ":starting_banner", 16),
      (store_add, "$g_presentation_banner_start", "$g_presentation_obj_profile_banner_selection_2", 1),
      (assign, ":num_valid_banners", 0),
      (try_for_range, ":cur_banner_mesh", banner_meshes_begin, banner_meshes_end_minus_one),
        (val_add, ":num_valid_banners", 1),
        (gt, ":num_valid_banners", ":starting_banner"),
        (le, ":num_valid_banners", ":ending_banner"),
        (create_image_button_overlay, reg1, ":cur_banner_mesh", ":cur_banner_mesh"),
        (position_set_x, pos1, ":x_pos"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 100),
        (overlay_set_size, reg1, pos1),
        (val_add, ":x_pos", 100),
        (ge, ":x_pos", 900),
        (assign, ":x_pos", 150),
        (val_sub, ":y_pos", 250),
      (try_end),
      (presentation_set_duration, 999999),
      ]),

    (ti_on_presentation_event_state_change, [
      (store_trigger_param_1, ":object"),
      (try_begin),
        (eq, ":object", "$g_presentation_obj_profile_banner_selection_1"),
        (val_add, "$g_presentation_page_no", 1),
        (val_mod, "$g_presentation_page_no", 8),
        (presentation_set_duration, 0),
        (start_presentation, "prsnt_game_profile_banner_selection"),
      (else_try),
        (eq, ":object", "$g_presentation_obj_profile_banner_selection_2"),
        (profile_set_banner_id, -1),
        (presentation_set_duration, 0),
      (else_try),
        (store_sub, ":selected_banner", ":object", "$g_presentation_banner_start"),
        (store_mul, ":page_adder", 16, "$g_presentation_page_no"),
        (val_add, ":selected_banner", ":page_adder"),
        (assign, ":num_valid_banners", 0),
        (assign, ":end_cond", banner_meshes_end_minus_one),
        (try_for_range, ":cur_banner_mesh", banner_meshes_begin, ":end_cond"),
          (try_begin),
            (eq, ":selected_banner", ":num_valid_banners"),
            (store_sub, ":selected_banner_index", ":cur_banner_mesh", banner_meshes_begin),
            (profile_set_banner_id, ":selected_banner_index"),
            (assign, ":end_cond", 0), #break
          (try_end),
          (val_add, ":num_valid_banners", 1),
        (try_end),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    ]),

  ("game_custom_battle_designer", prsntf_manual_end_only, "mesh_cb_ui_main", []),

  ("game_multiplayer_admin_panel", prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(team_set_faction, 0, 0),
      (team_set_faction, 1, 0),
      (start_multiplayer_mission, "mt_edit_scene", "scn_scene_1", 1),
      (presentation_set_duration, 100),
      ]),
    ]),

  ("game_before_quit", 0, "mesh_load_window", []),

  ("preset_message_small", prsntf_read_only|prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
      (try_begin),
        (eq, "$g_preset_message_type", preset_message_small),
        (assign, "$g_preset_message_type", 0),
        # keep the same as in prsnt_preset_message_* and script_preset_message
        (try_begin),
          (eq, "$g_preset_message_params", preset_message_item),
          (is_between, "$g_preset_message_value_1", 1, all_items_end),
          (str_store_item_name, s1, "$g_preset_message_value_1"),
        (else_try),
          (eq, "$g_preset_message_params", preset_message_agent),
          (agent_is_active, "$g_preset_message_value_1"),
          (str_store_agent_name, s1, "$g_preset_message_value_1"),
        (else_try),
          (eq, "$g_preset_message_params", preset_message_player),
          (player_is_active, "$g_preset_message_value_1"),
          (str_store_player_username, s1, "$g_preset_message_value_1"),
        (else_try),
          (is_between, "$g_preset_message_params", preset_message_faction, preset_message_faction_castle + 1),
          (is_between, "$g_preset_message_value_1", factions_begin, factions_end),
          (str_store_faction_name, s1, "$g_preset_message_value_1"),
          (faction_get_color, "$g_preset_message_color", "$g_preset_message_value_1"),
          (eq, "$g_preset_message_params", preset_message_faction_castle),
          (call_script, "script_str_store_castle_name", s2, "$g_preset_message_value_2"),
        (else_try),
          (assign, reg1, "$g_preset_message_value_1"),
          (assign, reg2, "$g_preset_message_value_2"),
        (try_end),
        # end keep same
        (create_text_overlay, ":overlay_id", "$g_preset_message_string_id", tf_center_justify|tf_with_outline),
        (overlay_set_color, ":overlay_id", "$g_preset_message_color"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_position, ":overlay_id", pos1),
        (presentation_set_duration, 300),
      (else_try),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    ]),

  ("preset_message_big", prsntf_read_only|prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
      (try_begin),
        (eq, "$g_preset_message_type", preset_message_big),
        (assign, "$g_preset_message_type", 0),
        # keep the same as in prsnt_preset_message_* and script_preset_message
        (try_begin),
          (eq, "$g_preset_message_params", preset_message_item),
          (is_between, "$g_preset_message_value_1", 1, all_items_end),
          (str_store_item_name, s1, "$g_preset_message_value_1"),
        (else_try),
          (eq, "$g_preset_message_params", preset_message_agent),
          (agent_is_active, "$g_preset_message_value_1"),
          (str_store_agent_name, s1, "$g_preset_message_value_1"),
        (else_try),
          (eq, "$g_preset_message_params", preset_message_player),
          (player_is_active, "$g_preset_message_value_1"),
          (str_store_player_username, s1, "$g_preset_message_value_1"),
        (else_try),
          (is_between, "$g_preset_message_params", preset_message_faction, preset_message_faction_castle + 1),
          (is_between, "$g_preset_message_value_1", factions_begin, factions_end),
          (str_store_faction_name, s1, "$g_preset_message_value_1"),
          (faction_get_color, "$g_preset_message_color", "$g_preset_message_value_1"),
          (eq, "$g_preset_message_params", preset_message_faction_castle),
          (call_script, "script_str_store_castle_name", s2, "$g_preset_message_value_2"),
        (else_try),
          (assign, reg1, "$g_preset_message_value_1"),
          (assign, reg2, "$g_preset_message_value_2"),
        (try_end),
        # end keep same
        (create_text_overlay, ":overlay_id", "$g_preset_message_string_id", tf_center_justify|tf_with_outline),
        (overlay_set_color, ":overlay_id", "$g_preset_message_color"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, ":overlay_id", pos1),
        (position_set_x, pos1, 2000),
        (position_set_y, pos1, 2000),
        (overlay_set_size, ":overlay_id", pos1),
        (presentation_set_duration, 500),
      (else_try),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    ]),

  ("read_object", prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
      (try_begin),
        (eq, "$g_preset_message_type", preset_message_read_object),
        (assign, "$g_preset_message_type", 0),
        (create_mesh_overlay, reg0, "mesh_mp_ingame_menu"),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (create_text_overlay, reg0, "$g_preset_message_string_id", tf_scrollable),
        (position_set_x, pos1, 285),
        (position_set_y, pos1, 155),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 405),
        (position_set_y, pos1, 470),
        (overlay_set_area_size, reg0, pos1),
        (overlay_set_color, reg0, "$g_preset_message_color"),

        (create_button_overlay, reg0, "str_done", tf_center_justify),
        (overlay_set_color, reg0, 0xFFFFFF),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 115),
        (overlay_set_position, reg0, pos1),

        (omit_key_once, key_escape),
        (presentation_set_duration, 999999),
      (else_try),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    (ti_on_presentation_event_state_change,
     [(clear_omitted_keys),
      (presentation_set_duration, 0),
      ]),
    (ti_on_presentation_run,
     [(store_trigger_param_1, ":cur_time"),
      (try_begin),
        (key_clicked, key_escape),
        (gt, ":cur_time", 200),
        (clear_omitted_keys),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    ]),

  ("display_agent_labels", prsntf_read_only|prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),

      (multiplayer_get_my_player, ":my_player"),
      (player_get_agent_id, ":my_agent", ":my_player"),
      (mission_cam_get_position, pos3),
      (try_for_agents, ":agent_id"),
        (agent_is_human, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (neq, ":agent_id", ":my_agent"),

        (agent_get_position, pos1, ":agent_id"),
        (position_move_z, pos1, 160),
        (agent_get_horse, ":horse", ":agent_id"),
        (try_begin),
          (ge, ":horse", 0),
          (position_move_z, pos1, 80),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos3),
        (le, ":distance", max_distance_to_see_labels),
        (position_has_line_of_sight_to_position, pos1, pos3),

        (position_move_z, pos1, 50),
        (position_get_screen_projection, pos2, pos1),
        (position_get_x, ":x_pos", pos2),
        (position_get_y, ":y_pos", pos2),
        (is_between, ":x_pos", -100, 1100),
        (is_between, ":y_pos", -100, 850),

        (str_clear, s2),
        (assign, ":color", 0xFF888888),
        (try_begin),
          (agent_is_non_player, ":agent_id"),
          (agent_get_troop_id, ":troop_id", ":agent_id"),
          (str_store_troop_name, s0, ":troop_id"),
        (else_try),
          (agent_get_player_id, ":player_id", ":agent_id"),
          (str_store_player_username, s2, ":player_id"),
          (player_get_slot, ":player_faction_id", ":player_id", slot_player_faction_id),
          (is_between, ":player_faction_id", factions_begin, factions_end),
          (str_store_faction_name, s3, ":player_faction_id"),
          (str_store_string, s0, "str_s2_s3"),
          (faction_get_color, ":color", ":player_faction_id"),
        (try_end),
        (copy_position, pos3, pos1),
        (position_move_z, pos3, 200),
        (position_get_screen_projection, pos4, pos3),
        (position_get_y, ":y_pos_up", pos4),
        (store_sub, ":height", ":y_pos_up", ":y_pos"),
        (val_mul, ":height", 10),
        (val_min, ":height", 2000),

        (create_text_overlay, reg2, s0, tf_center_justify|tf_with_outline),
        (overlay_set_position, reg2, pos2),
        (position_set_y, pos1, ":height"),
        (position_set_x, pos1, ":height"),
        (overlay_set_size, reg2, pos1),
        (overlay_set_color, reg2, ":color"),
      (try_end),
      (presentation_set_duration, 100),
      ]),
     (ti_on_presentation_run,
      [(store_trigger_param_1, ":cur_time"),
       (try_begin),
         (gt, ":cur_time", 20),
         (presentation_set_duration, 0),
         (eq, "$g_display_agent_labels", 1),
         (start_presentation, "prsnt_display_agent_labels"),
       (try_end),
       ]),
     ]),

  ("chat_box", prsntf_manual_end_only, 0,
   [(ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),

      (create_text_overlay, reg1, "$g_chat_box_string_id"),
      (overlay_set_color, reg1, 0xFFFFFFFF),
      (position_set_x, pos1, 200),
      (position_set_y, pos1, 530),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 1000),
      (position_set_y, pos1, 980),
      (overlay_set_size, reg1, pos1),

      (create_simple_text_box_overlay, "$g_presentation_obj_chat_box"),
      (position_set_x, pos1, 200),
      (position_set_y, pos1, 500),
      (overlay_set_position, "$g_presentation_obj_chat_box", pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_chat_box", pos1),
      (overlay_obtain_focus, "$g_presentation_obj_chat_box"),

      (presentation_set_duration, 999999),
      ]),
    (ti_on_presentation_event_state_change,
     [(store_trigger_param_1, ":object"),
      (try_begin),
        (eq, ":object", "$g_presentation_obj_chat_box"),
        (try_begin),
          (neg|key_clicked, key_left_mouse_button),
          (neg|key_clicked, key_escape),
          (neg|str_is_empty, s0),
          (is_between, "$g_chat_box_client_event", 0, 128),
          (try_begin),
            (is_between, "$g_chat_box_shift_client_event", 0, 128),
            (key_is_down, key_right_shift),
            (assign, ":client_event", "$g_chat_box_shift_client_event"),
          (else_try),
            (assign, ":client_event", "$g_chat_box_client_event"),
          (try_end),
          (multiplayer_send_string_to_server, ":client_event", s0),
        (try_end),
        (assign, "$g_chat_box_string_id", -1),
        (assign, "$g_chat_box_client_event", -1),
        (assign, "$g_chat_box_shift_client_event", -1),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    (ti_on_presentation_run,
     [(store_trigger_param_1, ":cur_time"),
      (try_begin),
        (key_clicked, key_escape),
        (gt, ":cur_time", 200),
        (assign, "$g_chat_box_string_id", -1),
        (assign, "$g_chat_box_client_event", -1),
        (assign, "$g_chat_box_shift_client_event", -1),
        (presentation_set_duration, 0),
      (try_end),
      ]),
    ]),

  ]
