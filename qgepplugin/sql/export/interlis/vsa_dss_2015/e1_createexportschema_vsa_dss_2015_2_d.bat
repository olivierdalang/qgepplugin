rem set variable to ili2pg*.jar, dbdatabase, dbpwd, ilipath etc.

java -jar ../ili2pg-3.12.2.jar --createEnumTxtCol --schemaimport --importTid --sqlEnableNull --createEnumTabs --createFk  --noSmartMapping --dbdatabase qgep --dbschema vsa_dss_2015_2_d --dbusr postgres --dbpwd yourpassword  --log createschema_VSA_DSS_2015_2_d.log VSA_DSS_2015_2_d.ili 