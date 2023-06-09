CNR training conf
training on cnr even patches 
validation on cnr odd patches

'--train_img', type=str, default='data/CNRPark-Patches-150x150/', 
--train_lab', type=str, default='data/splits/CNRParkAB/even.txt', 
'--test_img', type=str, default='data/CNRPark-Patches-150x150/', 
'--test_lab', type=str, default='data/splits/CNRParkAB/odd.txt',

CNR-EXT conf
training on all cnr+ext patches 
validating on cnr odd patches
'--train_img', type=str, default='data/PATCHES/', 
--train_lab', type=str, default='data/LABELS/all.txt', 
'--test_img', type=str, default='data/CNRPark-Patches-150x150/', 
'--test_lab', type=str, default='data/splits/CNRParkAB/odd.txt',
