from utility.sortCollection import Collection


#***************************************************
#Put NFT metadata and image files in the Inputs folder. Metadata and image filenames must be named numerically. Ex: 0.json, 0.png, 1.json, 1.png, ect...

#Define combinations of attributes below that should be excluded from the final NFT collection. Any NFT that contains all of the attributes in any of the lists below will be removed from the NFT collection.


exclude_attribute_combos=[
  ['some attribute value', 'some other attribute value'], #each line is a separate list of incompatible features
  ['do not mix this attribute value', 'with this attribute value', 'and this attribute value'],
  ['Gray', 'Weimereiner']
]


remove_by_name=[
  'Pixel Vizslas #6',
  'Pixel Vizslas #23'
]


#***************************************************


#do things----------------------------
newCollection=Collection('./Inputs') 
newCollection.excludeCombos(exclude_attribute_combos)
newCollection.removeNFT_by_name(remove_by_name)
newCollection.save()
print("Finished")

