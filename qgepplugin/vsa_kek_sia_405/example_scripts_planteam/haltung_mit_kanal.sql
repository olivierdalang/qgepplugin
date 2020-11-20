CREATE VIEW abwasser.schacht AS
SELECT 
AN.obj_id AS obj_id, -- Technische ID
verlauf, -- Geometrie
AN.bemerkung AS bemerkung,
AN.bezeichnung AS bezeichnung, -- Bezeichnung
laengeeffektiv, -- Schräge Länge
lichte_hoehe, 
AN.material AS material, 
plangefaelle, 
reibungsbeiwert, 
reliner_art, 
reliner_bautechnik, 
reliner_material, 
reliner_nennweite, 
ringsteifigkeit, 
wandrauhigkeit, 
rohrprofilref, 
nachhaltungspunktref, -- Kann für einen weiteren JOIN verwendet werden, hauptsächlich für die Anfangshöhe (und die Topologie)
vonhaltungspunktref, -- Kann für einen weiteren JOIN verwendet werden, hauptsächlich für die Endhöhe (und die Topologie)
AB.obj_id AS kanal_obj_id, 
baujahr, 
baulicherzustand,
baulos, 
AB.bemerkung AS kanal_bemerkung, 
AB.bezeichnung AS kanal_bezeichnung, 
bruttokosten, 
ersatzjahr, 
finanzierung, 
inspektionsintervall, 
sanierungsbedarf, 
standortname, 
astatus, 
subventionen, 
wbw_basisjahr, 
wbw_bauart, 
wiederbeschaffungswert, 
zugaenglichkeit, 
betreiberref, 
eigentuemerref, 
bettung_umhuellung, 
funktionhierarchisch, -- wichtig
funktionhydraulisch,
nutzungsart_geplant, 
nutzungsart_ist, -- wichtig
rohrlaenge, 
spuelintervall, 
verbindungsart, 
dimension1, 
dimension2

FROM abwasser.abwassernetzelement AN
LEFT JOIN abwasser.abwasserbauwerk AB ON AB.t_id=AN.abwasserbauwerkref
WHERE AN.t_type='haltung';
