host ='postgresdb'
username='primeuser'
database= 'NAMDB'
passwords='password'
# host ='postgresdb'
# # host='primestone-dev'
# # username='NAM_DB'
# # database= 'NAM_DB'
# # passwords='HeagweicyanVathGuAnetshyejFuthOo'
# q_page= "INSERT INTO page VALUES (nextval('page_sequence'), 1, bytea('./namdb_picturedata/predictions0.jpg')\
#             , false, 1, 1, 'swilde', current_timestamp, 'swilde', current_timestamp);" #fkeys= offer id, supplement id(NA, LV ids)



DARKNET_BINARY_LOCATION='/usr/local/primestone/darknet/darknet'
DARKNET_DATA_FILE='/usr/local/primestone/darknet/data/custom_data/obj.data'
DARKNET_CFG_FILE='/usr/local/primestone/darknet/data/custom_data/yolo-obj.cfg'
DARKNET_WEIGHTS='/usr/local/primestone/darknet/backup/yolo-obj_best.weights'
#DARKNET_THRESH=1'-iou_thresh'+' '+str(DARKNET_THRESH),

cmd= [DARKNET_BINARY_LOCATION,'detector','test\
',DARKNET_DATA_FILE,DARKNET_CFG_FILE,DARKNET_WEIGHTS,'-ext_output','-dont_show']


#cmd = DARKNET_BINARY_LOCATION + " detector test " + DARKNET_DATA_FILE + " " + DARKNET_CFG_FILE \
			#+ " " + DARKNET_WEIGHTS + " -thresh " + str(DARKNET_THRESH) + " -ext_output -dont_show"
print(cmd)