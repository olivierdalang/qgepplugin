from .qwat import Classes as QWAT
from .qgep import Classes as QGEP
from .wasser import Classes as WASSER
from .abwasser import Classes as ABWASSER

QWAT_TO_WASSER = {
    QWAT.node: [WASSER.hydraulischer_knoten],
    QWAT.hydrant: [WASSER.hydraulischer_knoten, WASSER.hydrant],
    QWAT.tank: [WASSER.hydraulischer_knoten, WASSER.wasserbehaelter],
    QWAT.pump: [WASSER.hydraulischer_knoten, WASSER.foerderanlage],
    QWAT.pipe: [WASSER.hydraulischer_strang, WASSER.leitung],
    # NOT MAPPED YET
    # AVAILABLE WASSER CLASSES : autres, autres_genre, baseclass, branchement_d_immeuble, branchement_d_immeuble_branchement_d_immeuble, branchement_d_immeuble_piece_isolante, composant, composant_genre, composant_materiau, composant_raccordement, conduite, conduite_assurance_contre_la_poussee, conduite_determination_planimetrique, conduite_fonction, conduite_genre_de_raccordement, conduite_isolation_exterieure, conduite_isolation_interieure, conduite_lit_de_pose, conduite_materiau, conduite_mode_de_pose, conduite_protection_cathodique, conduite_qualite_eau, conduite_rehabilitation_renovation, conduite_troncon_assoc, connexion_tubulaire, connexion_tubulaire_assurance_contre_la_poussee, connexion_tubulaire_genre, construction_speciale, construction_speciale_genre, construction_speciale_ligne, construction_speciale_materiau, construction_speciale_surface, determination_planimetrique, etat, etatvaleurs, halignment, hydrant, hydrant_genre, hydrant_materiau, installation, installation_d_approvisionnement_en_eau, installation_d_approvisionnement_en_eau_genre, installation_determination_altimetrique, installation_determination_planimetrique, installation_genre, installation_materiau, lieu_de_fuite, lieu_de_fuite_cause, lieu_de_fuite_genre, metaattributs, noeud_de_conduite, noeud_de_conduite_determination_altimetrique, noeud_de_conduite_determination_planimetrique, noeud_de_conduite_noeud_assoc, hydraulischer_knoten, hydraulischer_knoten_type_de_noeud, organe_de_fermeture, organe_de_fermeture_commande, organe_de_fermeture_etat_de_la_connexion, organe_de_fermeture_genre, organe_de_fermeture_materiau, organe_de_fermeture_sens_de_fermeture, point_de_conduite, point_de_conduite_determination_altimetrique, point_de_conduite_determination_planimetrique, point_de_conduite_genre, wasserbehaelter, wasserbehaelter_genre, wasserbehaelter_materiau, sia4055_lv95sia405_eaux_conduite_fonction, sia4055_lv95sia405_eaux_conduite_materiau, sia4055_lv95sia405_eaux_construction_speciale_genre, sia4055_lv95sia405_eaux_cs_conduite_determination_planmtrque, sia4055_lv95sia405_eaux_installation_genre, sia405_15_lv95sia405_eaux_cs_conduite, sia405_15_lv95sia405_eaux_cs_conduite_texte, sia405_15_lv95sia405_eaux_cs_conduite_texteassoc, sia405_15_lv95sia405_eaux_cs_construction_speciale, sia405_15_lv95sia405_eaux_cs_construction_speciale_ligne, sia405_15_lv95sia405_eaux_cs_construction_speciale_lignessoc, sia405_15_lv95sia405_eaux_cs_construction_speciale_surface, sia405_15_lv95sia405_eaux_cs_construction_speciale_surfcssoc, sia405_15_lv95sia405_eaux_cs_construction_speciale_texte, sia405_15_lv95sia405_eaux_cs_construction_speciale_textessoc, sia405_15_lv95sia405_eaux_cs_installation, sia405_15_lv95sia405_eaux_cs_noeud_de_conduite, sia405_15_lv95sia405_eaux_cs_noeud_de_conduite_texte, sia405_15_lv95sia405_eaux_cs_noeud_de_conduite_texteassoc, sia405_baseclass, sia405_symbolepos, sia405_textepos, foerderanlage_genre, symbolepos, t_ili2db_attrname, t_ili2db_basket, t_ili2db_classname, t_ili2db_dataset, t_ili2db_inheritance, t_ili2db_model, t_ili2db_settings, textepos, hydraulischer_strang, type_de_plan, valignment
    # QWAT.bedding: [WASSER.REPLACE_ME],
    # QWAT.chamber: [WASSER.REPLACE_ME],
    # QWAT.cistern: [WASSER.REPLACE_ME],
    # QWAT.consumptionzone: [WASSER.REPLACE_ME],
    # QWAT.cover: [WASSER.REPLACE_ME],
    # QWAT.cover_type: [WASSER.REPLACE_ME],
    # QWAT.crossing: [WASSER.REPLACE_ME],
    # QWAT.damage: [WASSER.REPLACE_ME],
    # QWAT.distributor: [WASSER.REPLACE_ME],
    # QWAT.district: [WASSER.REPLACE_ME],
    # QWAT.folder: [WASSER.REPLACE_ME],
    # QWAT.hydrant_material: [WASSER.REPLACE_ME],
    # QWAT.hydrant_model_inf: [WASSER.REPLACE_ME],
    # QWAT.hydrant_model_sup: [WASSER.REPLACE_ME],
    # QWAT.hydrant_output: [WASSER.REPLACE_ME],
    # QWAT.hydrant_provider: [WASSER.REPLACE_ME],
    # QWAT.installation: [WASSER.REPLACE_ME],
    # QWAT.leak: [WASSER.REPLACE_ME],
    # QWAT.leak_cause: [WASSER.REPLACE_ME],
    # QWAT.meter: [WASSER.REPLACE_ME],
    # QWAT.meter_reference: [WASSER.REPLACE_ME],
    # QWAT.network_element: [WASSER.REPLACE_ME],
    # QWAT.nominal_diameter: [WASSER.REPLACE_ME],
    # QWAT.object_reference: [WASSER.REPLACE_ME],
    # QWAT.overflow: [WASSER.REPLACE_ME],
    # QWAT.part: [WASSER.REPLACE_ME],
    # QWAT.part_type: [WASSER.REPLACE_ME],
    # QWAT.pipe_function: [WASSER.REPLACE_ME],
    # QWAT.pipe_installmethod: [WASSER.REPLACE_ME],
    # QWAT.pipe_material: [WASSER.REPLACE_ME],
    # QWAT.pipe_protection: [WASSER.REPLACE_ME],
    # QWAT.precision: [WASSER.REPLACE_ME],
    # QWAT.precisionalti: [WASSER.REPLACE_ME],
    # QWAT.pressurecontrol_type: [WASSER.REPLACE_ME],
    # QWAT.pressurezone: [WASSER.REPLACE_ME],
    # QWAT.printmap: [WASSER.REPLACE_ME],
    # QWAT.protectionzone: [WASSER.REPLACE_ME],
    # QWAT.protectionzone_type: [WASSER.REPLACE_ME],
    # QWAT.pump_operating: [WASSER.REPLACE_ME],
    # QWAT.pump_type: [WASSER.REPLACE_ME],
    # QWAT.remote: [WASSER.REPLACE_ME],
    # QWAT.remote_type: [WASSER.REPLACE_ME],
    # QWAT.samplingpoint: [WASSER.REPLACE_ME],
    # QWAT.source: [WASSER.REPLACE_ME],
    # QWAT.source_quality: [WASSER.REPLACE_ME],
    # QWAT.source_type: [WASSER.REPLACE_ME],
    # QWAT.status: [WASSER.REPLACE_ME],
    # QWAT.subscriber: [WASSER.REPLACE_ME],
    # QWAT.subscriber_reference: [WASSER.REPLACE_ME],
    # QWAT.subscriber_type: [WASSER.REPLACE_ME],
    # QWAT.survey_type: [WASSER.REPLACE_ME],
    # QWAT.surveypoint: [WASSER.REPLACE_ME],
    # QWAT.tank_firestorage: [WASSER.REPLACE_ME],
    # QWAT.treatment: [WASSER.REPLACE_ME],
    # QWAT.valve: [WASSER.REPLACE_ME],
    # QWAT.valve_actuation: [WASSER.REPLACE_ME],
    # QWAT.valve_function: [WASSER.REPLACE_ME],
    # QWAT.valve_type: [WASSER.REPLACE_ME],
    # QWAT.visible: [WASSER.REPLACE_ME],
    # QWAT.watertype: [WASSER.REPLACE_ME],
    # QWAT.worker: [WASSER.REPLACE_ME],
}


QGEP_TO_ABWASSER = {
    QGEP.organisation: [ABWASSER.organisation, ABWASSER.metaattribute],
    QGEP.channel: [ABWASSER.kanal],
    QGEP.manhole: [ABWASSER.normschacht],
    QGEP.discharge_point: [ABWASSER.einleitstelle],
    QGEP.special_structure: [ABWASSER.spezialbauwerk],
    QGEP.infiltration_installation: [ABWASSER.versickerungsanlage],
    QGEP.pipe_profile: [ABWASSER.rohrprofil],
    QGEP.reach_point: [ABWASSER.haltungspunkt],
    QGEP.wastewater_node: [ABWASSER.abwasserknoten],
    QGEP.reach: [ABWASSER.haltung],
    QGEP.dryweather_downspout: [ABWASSER.trockenwetterfallrohr],
    QGEP.access_aid: [ABWASSER.einstiegshilfe],
    QGEP.dryweather_flume: [ABWASSER.trockenwetterrinne],
    QGEP.cover: [ABWASSER.deckel],
    QGEP.benching: [ABWASSER.bankett],
    # NOT MAPPED YET
    # AVAILABLE ABWASSER CLASSES : abwasserbauwerk, abwasserknoten, abwassernetzelement, bankett, baseclass, bauwerksteil, datei, datentraeger, deckel, einleitstelle, einstiegshilfe, erhaltungsereignis, haltung, haltung_alternativverlauf, haltungspunkt, kanal, kanalschaden, metaattribute, normschacht, normschachtschaden, organisation, organisation_teil_vonassoc, rohrprofil, schaden, sia405_baseclass, sia405_symbolpos, sia405_textpos, spezialbauwerk, symbolpos, t_ili2db_attrname, t_ili2db_basket, t_ili2db_classname, t_ili2db_dataset, t_ili2db_inheritance, t_ili2db_model, t_ili2db_settings, textpos, trockenwetterfallrohr, trockenwetterrinne, untersuchung, versickerungsanlage, videozaehlerstand
    # QGEP.access_aid: [ABWASSER.REPLACE_ME],
    # QGEP.access_aid_kind: [ABWASSER.REPLACE_ME],
    # QGEP.accident: [ABWASSER.REPLACE_ME],
    # QGEP.administrative_office: [ABWASSER.REPLACE_ME],
    # QGEP.aquifier: [ABWASSER.REPLACE_ME],
    # QGEP.backflow_prevention: [ABWASSER.REPLACE_ME],
    # QGEP.backflow_prevention_kind: [ABWASSER.REPLACE_ME],
    # QGEP.bathing_area: [ABWASSER.REPLACE_ME],
    # QGEP.benching: [ABWASSER.REPLACE_ME],
    # QGEP.benching_kind: [ABWASSER.REPLACE_ME],
    # QGEP.blocking_debris: [ABWASSER.REPLACE_ME],
    # QGEP.building: [ABWASSER.REPLACE_ME],
    # QGEP.canton: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_direct_discharge_current: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_direct_discharge_planned: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_drainage_system_current: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_drainage_system_planned: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_infiltration_current: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_infiltration_planned: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_retention_current: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_retention_planned: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_text: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_text_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_text_texthali: [ABWASSER.REPLACE_ME],
    # QGEP.catchment_area_text_textvali: [ABWASSER.REPLACE_ME],
    # QGEP.channel: [ABWASSER.REPLACE_ME],
    # QGEP.channel_bedding_encasement: [ABWASSER.REPLACE_ME],
    # QGEP.channel_connection_type: [ABWASSER.REPLACE_ME],
    # QGEP.channel_function_hierarchic: [ABWASSER.REPLACE_ME],
    # QGEP.channel_function_hydraulic: [ABWASSER.REPLACE_ME],
    # QGEP.channel_usage_current: [ABWASSER.REPLACE_ME],
    # QGEP.channel_usage_planned: [ABWASSER.REPLACE_ME],
    # QGEP.chute: [ABWASSER.REPLACE_ME],
    # QGEP.chute_kind: [ABWASSER.REPLACE_ME],
    # QGEP.chute_material: [ABWASSER.REPLACE_ME],
    # QGEP.connection_object: [ABWASSER.REPLACE_ME],
    # QGEP.control_center: [ABWASSER.REPLACE_ME],
    # QGEP.cooperative: [ABWASSER.REPLACE_ME],
    # QGEP.cover: [ABWASSER.REPLACE_ME],
    # QGEP.cover_cover_shape: [ABWASSER.REPLACE_ME],
    # QGEP.cover_fastening: [ABWASSER.REPLACE_ME],
    # QGEP.cover_material: [ABWASSER.REPLACE_ME],
    # QGEP.cover_positional_accuracy: [ABWASSER.REPLACE_ME],
    # QGEP.cover_sludge_bucket: [ABWASSER.REPLACE_ME],
    # QGEP.cover_venting: [ABWASSER.REPLACE_ME],
    # QGEP.dam: [ABWASSER.REPLACE_ME],
    # QGEP.dam_kind: [ABWASSER.REPLACE_ME],
    # QGEP.damage: [ABWASSER.REPLACE_ME],
    # QGEP.damage_channel_channel_damage_code: [ABWASSER.REPLACE_ME],
    # QGEP.damage_connection: [ABWASSER.REPLACE_ME],
    # QGEP.damage_manhole: [ABWASSER.REPLACE_ME],
    # QGEP.damage_manhole_manhole_damage_code: [ABWASSER.REPLACE_ME],
    # QGEP.damage_manhole_manhole_shaft_area: [ABWASSER.REPLACE_ME],
    # QGEP.damage_single_damage_class: [ABWASSER.REPLACE_ME],
    # QGEP.data_media: [ABWASSER.REPLACE_ME],
    # QGEP.data_media_kind: [ABWASSER.REPLACE_ME],
    # QGEP.discharge_point: [ABWASSER.REPLACE_ME],
    # QGEP.discharge_point_relevance: [ABWASSER.REPLACE_ME],
    # QGEP.drainage_system: [ABWASSER.REPLACE_ME],
    # QGEP.drainage_system_kind: [ABWASSER.REPLACE_ME],
    # QGEP.dryweather_downspout: [ABWASSER.REPLACE_ME],
    # QGEP.dryweather_flume: [ABWASSER.REPLACE_ME],
    # QGEP.dryweather_flume_material: [ABWASSER.REPLACE_ME],
    # QGEP.electric_equipment: [ABWASSER.REPLACE_ME],
    # QGEP.electric_equipment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.electromechanical_equipment: [ABWASSER.REPLACE_ME],
    # QGEP.electromechanical_equipment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.examination: [ABWASSER.REPLACE_ME],
    # QGEP.examination_recording_type: [ABWASSER.REPLACE_ME],
    # QGEP.examination_weather: [ABWASSER.REPLACE_ME],
    # QGEP.file: [ABWASSER.REPLACE_ME],
    # QGEP.file_class: [ABWASSER.REPLACE_ME],
    # QGEP.file_kind: [ABWASSER.REPLACE_ME],
    # QGEP.fish_pass: [ABWASSER.REPLACE_ME],
    # QGEP.ford: [ABWASSER.REPLACE_ME],
    # QGEP.fountain: [ABWASSER.REPLACE_ME],
    # QGEP.ground_water_protection_perimeter: [ABWASSER.REPLACE_ME],
    # QGEP.groundwater_protection_zone: [ABWASSER.REPLACE_ME],
    # QGEP.groundwater_protection_zone_kind: [ABWASSER.REPLACE_ME],
    # QGEP.hazard_source: [ABWASSER.REPLACE_ME],
    # QGEP.hq_relation: [ABWASSER.REPLACE_ME],
    # QGEP.hydr_geom_relation: [ABWASSER.REPLACE_ME],
    # QGEP.hydr_geometry: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data_is_overflowing: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data_main_weir_kind: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data_pump_characteristics: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data_pump_usage_current: [ABWASSER.REPLACE_ME],
    # QGEP.hydraulic_char_data_status: [ABWASSER.REPLACE_ME],
    # QGEP.individual_surface: [ABWASSER.REPLACE_ME],
    # QGEP.individual_surface_function: [ABWASSER.REPLACE_ME],
    # QGEP.individual_surface_pavement: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_defects: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_emergency_spillway: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_kind: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_labeling: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_seepage_utilization: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_vehicle_access: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_installation_watertightness: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_zone: [ABWASSER.REPLACE_ME],
    # QGEP.infiltration_zone_infiltration_capacity: [ABWASSER.REPLACE_ME],
    # QGEP.lake: [ABWASSER.REPLACE_ME],
    # QGEP.leapingweir: [ABWASSER.REPLACE_ME],
    # QGEP.leapingweir_opening_shape: [ABWASSER.REPLACE_ME],
    # QGEP.lock: [ABWASSER.REPLACE_ME],
    # QGEP.maintenance_event: [ABWASSER.REPLACE_ME],
    # QGEP.maintenance_event_kind: [ABWASSER.REPLACE_ME],
    # QGEP.maintenance_event_status: [ABWASSER.REPLACE_ME],
    # QGEP.manhole_function: [ABWASSER.REPLACE_ME],
    # QGEP.manhole_material: [ABWASSER.REPLACE_ME],
    # QGEP.manhole_surface_inflow: [ABWASSER.REPLACE_ME],
    # QGEP.measurement_result: [ABWASSER.REPLACE_ME],
    # QGEP.measurement_result_measurement_type: [ABWASSER.REPLACE_ME],
    # QGEP.measurement_series: [ABWASSER.REPLACE_ME],
    # QGEP.measurement_series_kind: [ABWASSER.REPLACE_ME],
    # QGEP.measuring_device: [ABWASSER.REPLACE_ME],
    # QGEP.measuring_device_kind: [ABWASSER.REPLACE_ME],
    # QGEP.measuring_point: [ABWASSER.REPLACE_ME],
    # QGEP.measuring_point_damming_device: [ABWASSER.REPLACE_ME],
    # QGEP.measuring_point_purpose: [ABWASSER.REPLACE_ME],
    # QGEP.mechanical_pretreatment: [ABWASSER.REPLACE_ME],
    # QGEP.mechanical_pretreatment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.municipality: [ABWASSER.REPLACE_ME],
    # QGEP.mutation: [ABWASSER.REPLACE_ME],
    # QGEP.mutation_kind: [ABWASSER.REPLACE_ME],
    # QGEP.overflow: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_actuation: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_adjustability: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_char: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_char_kind_overflow_characteristic: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_char_overflow_characteristic_digital: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_control: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_function: [ABWASSER.REPLACE_ME],
    # QGEP.overflow_signal_transmission: [ABWASSER.REPLACE_ME],
    # QGEP.param_ca_general: [ABWASSER.REPLACE_ME],
    # QGEP.param_ca_mouse1: [ABWASSER.REPLACE_ME],
    # QGEP.passage: [ABWASSER.REPLACE_ME],
    # QGEP.pipe_profile: [ABWASSER.REPLACE_ME],
    # QGEP.pipe_profile_profile_type: [ABWASSER.REPLACE_ME],
    # QGEP.planning_zone: [ABWASSER.REPLACE_ME],
    # QGEP.planning_zone_kind: [ABWASSER.REPLACE_ME],
    # QGEP.prank_weir: [ABWASSER.REPLACE_ME],
    # QGEP.prank_weir_weir_edge: [ABWASSER.REPLACE_ME],
    # QGEP.prank_weir_weir_kind: [ABWASSER.REPLACE_ME],
    # QGEP.private: [ABWASSER.REPLACE_ME],
    # QGEP.profile_geometry: [ABWASSER.REPLACE_ME],
    # QGEP.pump: [ABWASSER.REPLACE_ME],
    # QGEP.pump_contruction_type: [ABWASSER.REPLACE_ME],
    # QGEP.pump_placement_of_actuation: [ABWASSER.REPLACE_ME],
    # QGEP.pump_placement_of_pump: [ABWASSER.REPLACE_ME],
    # QGEP.pump_usage_current: [ABWASSER.REPLACE_ME],
    # QGEP.re_maintenance_event_wastewater_structure: [ABWASSER.REPLACE_ME],
    # QGEP.reach: [ABWASSER.REPLACE_ME],
    # QGEP.reach_elevation_determination: [ABWASSER.REPLACE_ME],
    # QGEP.reach_horizontal_positioning: [ABWASSER.REPLACE_ME],
    # QGEP.reach_inside_coating: [ABWASSER.REPLACE_ME],
    # QGEP.reach_material: [ABWASSER.REPLACE_ME],
    # QGEP.reach_point: [ABWASSER.REPLACE_ME],
    # QGEP.reach_point_elevation_accuracy: [ABWASSER.REPLACE_ME],
    # QGEP.reach_point_outlet_shape: [ABWASSER.REPLACE_ME],
    # QGEP.reach_reliner_material: [ABWASSER.REPLACE_ME],
    # QGEP.reach_relining_construction: [ABWASSER.REPLACE_ME],
    # QGEP.reach_relining_kind: [ABWASSER.REPLACE_ME],
    # QGEP.reach_text: [ABWASSER.REPLACE_ME],
    # QGEP.reach_text_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.reach_text_texthali: [ABWASSER.REPLACE_ME],
    # QGEP.reach_text_textvali: [ABWASSER.REPLACE_ME],
    # QGEP.reservoir: [ABWASSER.REPLACE_ME],
    # QGEP.retention_body: [ABWASSER.REPLACE_ME],
    # QGEP.retention_body_kind: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_control_grade_of_river: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_river_control_type: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_shores: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_side: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_utilisation_of_shore_surroundings: [ABWASSER.REPLACE_ME],
    # QGEP.river_bank_vegetation: [ABWASSER.REPLACE_ME],
    # QGEP.river_bed: [ABWASSER.REPLACE_ME],
    # QGEP.river_bed_control_grade_of_river: [ABWASSER.REPLACE_ME],
    # QGEP.river_bed_kind: [ABWASSER.REPLACE_ME],
    # QGEP.river_bed_river_control_type: [ABWASSER.REPLACE_ME],
    # QGEP.river_kind: [ABWASSER.REPLACE_ME],
    # QGEP.rock_ramp: [ABWASSER.REPLACE_ME],
    # QGEP.rock_ramp_stabilisation: [ABWASSER.REPLACE_ME],
    # QGEP.sector_water_body: [ABWASSER.REPLACE_ME],
    # QGEP.sector_water_body_kind: [ABWASSER.REPLACE_ME],
    # QGEP.sludge_treatment: [ABWASSER.REPLACE_ME],
    # QGEP.sludge_treatment_stabilisation: [ABWASSER.REPLACE_ME],
    # QGEP.solids_retention: [ABWASSER.REPLACE_ME],
    # QGEP.solids_retention_type: [ABWASSER.REPLACE_ME],
    # QGEP.special_structure: [ABWASSER.REPLACE_ME],
    # QGEP.special_structure_bypass: [ABWASSER.REPLACE_ME],
    # QGEP.special_structure_emergency_spillway: [ABWASSER.REPLACE_ME],
    # QGEP.special_structure_function: [ABWASSER.REPLACE_ME],
    # QGEP.special_structure_stormwater_tank_arrangement: [ABWASSER.REPLACE_ME],
    # QGEP.structure_part: [ABWASSER.REPLACE_ME],
    # QGEP.structure_part_renovation_demand: [ABWASSER.REPLACE_ME],
    # QGEP.substance: [ABWASSER.REPLACE_ME],
    # QGEP.surface_runoff_parameters: [ABWASSER.REPLACE_ME],
    # QGEP.surface_water_bodies: [ABWASSER.REPLACE_ME],
    # QGEP.symbol_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.tank_cleaning: [ABWASSER.REPLACE_ME],
    # QGEP.tank_cleaning_type: [ABWASSER.REPLACE_ME],
    # QGEP.tank_emptying: [ABWASSER.REPLACE_ME],
    # QGEP.tank_emptying_type: [ABWASSER.REPLACE_ME],
    # QGEP.text_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.text_texthali: [ABWASSER.REPLACE_ME],
    # QGEP.text_textvali: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit_actuation: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit_adjustability: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit_control: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit_kind: [ABWASSER.REPLACE_ME],
    # QGEP.throttle_shut_off_unit_signal_transmission: [ABWASSER.REPLACE_ME],
    # QGEP.txt_symbol: [ABWASSER.REPLACE_ME],
    # QGEP.txt_text: [ABWASSER.REPLACE_ME],
    # QGEP.waste_water_association: [ABWASSER.REPLACE_ME],
    # QGEP.waste_water_treatment: [ABWASSER.REPLACE_ME],
    # QGEP.waste_water_treatment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.waste_water_treatment_plant: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_networkelement: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_node: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_accessibility: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_financing: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_renovation_necessity: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_rv_construction_type: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_status: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_structure_condition: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_symbol: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_symbol_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_text: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_text_plantype: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_text_texthali: [ABWASSER.REPLACE_ME],
    # QGEP.wastewater_structure_text_textvali: [ABWASSER.REPLACE_ME],
    # QGEP.water_body_protection_sector: [ABWASSER.REPLACE_ME],
    # QGEP.water_body_protection_sector_kind: [ABWASSER.REPLACE_ME],
    # QGEP.water_catchment: [ABWASSER.REPLACE_ME],
    # QGEP.water_catchment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.water_control_structure: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_algae_growth: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_altitudinal_zone: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_dead_wood: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_depth_variability: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_discharge_regime: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_ecom_classification: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_kind: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_length_profile: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_macrophyte_coverage: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_section_morphology: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_slope: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_utilisation: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_water_hardness: [ABWASSER.REPLACE_ME],
    # QGEP.water_course_segment_width_variability: [ABWASSER.REPLACE_ME],
    # QGEP.wwtp_energy_use: [ABWASSER.REPLACE_ME],
    # QGEP.wwtp_structure_kind: [ABWASSER.REPLACE_ME],
    # QGEP.zone: [ABWASSER.REPLACE_ME],
}
