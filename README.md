Download data from here: http://cnrpark.it/ or run get_dataset.sh

# CNR training conf
### Training on cnr even patches 
### Validation on cnr odd patches

```
'--train_img', type=str, default='data/CNRPark-Patches-150x150/'
'--train_lab', type=str, default='data/splits/CNRParkAB/even.txt'
'--test_img', type=str, default='data/CNRPark-Patches-150x150/'
'--test_lab', type=str, default='data/splits/CNRParkAB/odd.txt'
```


# CNR-EXT config
### Training on all cnr+ext patches 
### Validating on cnr odd patches

```
'--train_img', type=str, default='data/PATCHES/'
--train_lab', type=str, default='data/LABELS/all.txt'
'--test_img', type=str, default='data/CNRPark-Patches-150x150/'
'--test_lab', type=str, default='data/splits/CNRParkAB/odd.txt'
```
