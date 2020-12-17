print("Exporting QWAT.pipe -> WASSER.conduite")
for row in session.query(QWAT.pipe):
    # AVAILABLE ROW FIELDS : REF_crossing_pipe2, REF_pump_fk_pipe_in, _decl_class_registry, _diff_elevation, _geometry_alt1_used, _geometry_alt2_used, _length2d, _length3d, _printmaps, _sa_class_manager, _sa_decl_prepare, _sa_raise_deferred_config, _schema_visible, _valve_closed, _valve_count, bedding, classes, distributor, district, fk_bedding, fk_distributor, fk_district, fk_folder, fk_function, fk_installmethod, fk_locationtype, fk_material, fk_node_a, fk_node_b, fk_parent, fk_precision, fk_pressurezone, fk_printmap, fk_protection, fk_status, fk_watertype, folder, geometry, geometry_alt1, geometry_alt2, id, label_1_text, label_1_visible, label_2_text, label_2_visible, metadata, node, pipe, pipe_function, pipe_installmethod, pipe_material, pipe_protection, precision, prepare, pressure_nominal, pressurezone, remark, schema_force_visible, status, tunnel_or_bridge, update_geometry_alt1, update_geometry_alt2, visible, watertype, year, year_end, year_rehabilitation
    session.add(
        WASSER.conduite(
            # _decl_class_registry=row.REPLACE_ME,
            # _sa_class_manager=row.REPLACE_ME,
            # _sa_decl_prepare=row.REPLACE_ME,
            # _sa_raise_deferred_config=row.REPLACE_ME,
            # acondition=row.REPLACE_ME,
            # annee_de_construction=row.REPLACE_ME,
            # assurance_contre_la_poussee=row.REPLACE_ME,
            # classes=row.REPLACE_ME,
            # concessionnaire=row.REPLACE_ME,
            # couverture=row.REPLACE_ME,
            # determination_planimetrique=row.REPLACE_ME,
            # diametre=row.REPLACE_ME,
            # diametre_exterieur=row.REPLACE_ME,
            # diametre_interieur=row.REPLACE_ME,
            # entretien=row.REPLACE_ME,
            # etat=row.REPLACE_ME,
            # exploitant=row.REPLACE_ME,
            # fonction=row.REPLACE_ME,
            # genre_de_raccordement=row.REPLACE_ME,
            # geometrie=row.REPLACE_ME,
            # isolation_exterieure=row.REPLACE_ME,
            # isolation_interieure=row.REPLACE_ME,
            # largeur_nominale=row.REPLACE_ME,
            # lit_de_pose=row.REPLACE_ME,
            # longueur=row.REPLACE_ME,
            # materiau=row.REPLACE_ME,
            # metadata=row.REPLACE_ME,
            # mode_de_pose=row.REPLACE_ME,
            # nom_numero=row.REPLACE_ME,
            # obj_id=row.REPLACE_ME,
            # prepare=row.REPLACE_ME,
            # pression_de_fonctionnement_admissible=row.REPLACE_ME,
            # pression_exploitation=row.REPLACE_ME,
            # proprietaire=row.REPLACE_ME,
            # protection_cathodique=row.REPLACE_ME,
            # qualite_eau=row.REPLACE_ME,
            # rehabilitation_renovation=row.REPLACE_ME,
            # remarque=row.REPLACE_ME,
            # responsable_entretien=row.REPLACE_ME,
            # rugosite_hydraulique=row.REPLACE_ME,
            # t_id=row.REPLACE_ME,
            # t_ili_tid=row.REPLACE_ME,
            # troncon_hydraulique=row.REPLACE_ME,
            # tronconref=row.REPLACE_ME,
            # zone_de_pression=row.REPLACE_ME,
        )
    )
    print(".", end="")
print("done")

print("Exporting QWAT.hydrant -> WASSER.hydrant")
for row in session.query(QWAT.hydrant):
    # AVAILABLE ROW FIELDS : _decl_class_registry, _sa_class_manager, _sa_decl_prepare, _sa_raise_deferred_config, classes, fk_material, fk_model_inf, fk_model_sup, fk_output, fk_provider, flow, hydrant_material, hydrant_model_inf, hydrant_model_sup, hydrant_output, hydrant_provider, id, marked, metadata, network_element, observation_date, observation_source, prepare, pressure_dynamic, pressure_static, underground
    session.add(
        WASSER.hydrant(
            # _decl_class_registry=row.REPLACE_ME,
            # _sa_class_manager=row.REPLACE_ME,
            # _sa_decl_prepare=row.REPLACE_ME,
            # _sa_raise_deferred_config=row.REPLACE_ME,
            # acondition=row.REPLACE_ME,
            # altitude=row.REPLACE_ME,
            # annee_de_construction=row.REPLACE_ME,
            # atype=row.REPLACE_ME,
            # classes=row.REPLACE_ME,
            # determination_altimetrique=row.REPLACE_ME,
            # determination_planimetrique=row.REPLACE_ME,
            # dimension=row.REPLACE_ME,
            # fabricant=row.REPLACE_ME,
            # genre=row.REPLACE_ME,
            # geometrie=row.REPLACE_ME,
            # materiau=row.REPLACE_ME,
            # metadata=row.REPLACE_ME,
            # noeud_hydraulique=row.REPLACE_ME,
            # noeudref=row.REPLACE_ME,
            # nom_numero=row.REPLACE_ME,
            # obj_id=row.REPLACE_ME,
            # prepare=row.REPLACE_ME,
            # pression_de_distribution=row.REPLACE_ME,
            # pression_ecoulement=row.REPLACE_ME,
            # proprietaire=row.REPLACE_ME,
            # remarque=row.REPLACE_ME,
            # soutirage=row.REPLACE_ME,
            # symboleori=row.REPLACE_ME,
            # t_id=row.REPLACE_ME,
            # t_ili_tid=row.REPLACE_ME,
            # zone_de_pression=row.REPLACE_ME,
        )
    )
    print(".", end="")
print("done")

print("Exporting QWAT.tank -> WASSER.reservoir_d_eau")
for row in session.query(QWAT.tank):
    # AVAILABLE ROW FIELDS : REF_pressurecontrol_id_fkey, _cistern1_litrepercm, _cistern2_litrepercm, _decl_class_registry, _litrepercm, _sa_class_manager, _sa_decl_prepare, _sa_raise_deferred_config, altitude_apron, altitude_overflow, cistern, cistern1_dimension_1, cistern1_dimension_2, cistern1_fk_type, cistern1_storage, cistern2_dimension_1, cistern2_dimension_2, cistern2_fk_type, cistern2_storage, classes, eca, fire_remote, fire_valve, fk_overflow, fk_parent, fk_remote, fk_tank_firestorage, fk_watertype, geometry_polygon, height_max, id, installation, metadata, name, network_element, open_water_surface, overflow, parcel, prepare, remote_type, storage_fire, storage_supply, storage_total, tank_firestorage, watertype
    session.add(
        WASSER.reservoir_d_eau(
            # _decl_class_registry=row.REPLACE_ME,
            # _sa_class_manager=row.REPLACE_ME,
            # _sa_decl_prepare=row.REPLACE_ME,
            # _sa_raise_deferred_config=row.REPLACE_ME,
            # acondition=row.REPLACE_ME,
            # altitude=row.REPLACE_ME,
            # annee_de_construction=row.REPLACE_ME,
            # capacite_de_stockage=row.REPLACE_ME,
            # classes=row.REPLACE_ME,
            # determination_altimetrique=row.REPLACE_ME,
            # determination_planimetrique=row.REPLACE_ME,
            # genre=row.REPLACE_ME,
            # geometrie=row.REPLACE_ME,
            # hauteur_de_refoulement=row.REPLACE_ME,
            # materiau=row.REPLACE_ME,
            # metadata=row.REPLACE_ME,
            # noeud_hydraulique=row.REPLACE_ME,
            # noeudref=row.REPLACE_ME,
            # nom_numero=row.REPLACE_ME,
            # obj_id=row.REPLACE_ME,
            # prepare=row.REPLACE_ME,
            # proprietaire=row.REPLACE_ME,
            # puissance=row.REPLACE_ME,
            # remarque=row.REPLACE_ME,
            # reserve_eau_alimentation=row.REPLACE_ME,
            # reserve_eau_incendie=row.REPLACE_ME,
            # revetement=row.REPLACE_ME,
            # symboleori=row.REPLACE_ME,
            # t_id=row.REPLACE_ME,
            # t_ili_tid=row.REPLACE_ME,
            # zone_de_pression=row.REPLACE_ME,
        )
    )
    print(".", end="")
print("done")

