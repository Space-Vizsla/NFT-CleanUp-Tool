import os
import json
import shutil

class NFT:
  def __init__(self, metaDataFile):
    f=open('./Inputs/'+metaDataFile)
    self.metaDataFile=metaDataFile
    self.metaData=json.load(f)
    self.image=self.metaData['image']
    self.name=self.metaData['name']
    self.attributes_parsed=json.dumps(self.metaData['attributes'])
    self.metadata_parsed=json.dumps(self.metaData)

  def updateValue(self, key, newValue):
    self.metaData[key]=newValue

  def renumber(self, number): #renumber name & image number in metadata
    x=self.metaData['image'].split('.')
    x[0]=str(number)
    y=self.metaData['name'].split('#')
    y[1]=str(number+1)
    self.metaData['image']='.'.join(x)
    self.metaData['name']='#'.join(y)
    self.metaData['properties']['files'][0]['uri']='.'.join(x)


class Collection:
  def __init__(self, filepath):
    def getFiles(path):
      def customkey(file):
        x=file.split('.')
        return int(x[0])
      files=os.listdir(path)
      return sorted(files, key=customkey)

    self.allFiles=getFiles(filepath)
    metaFiles=[]
    self.collection=[]
    for file in self.allFiles:
      if ".txt" in file or ".json" in file:
        metaFiles.append(file)
    for i in range(0, len(metaFiles)):
      self.collection.append(NFT(metaFiles[i]))
        
  def excludeCombos(self, excludeAttributes):
    j=0
    for nft in self.collection:
      for exclusion in excludeAttributes:
        i=0
        for item in exclusion:
          if item in nft.attributes_parsed:
            i+=1
        if i==len(exclusion):
          print('NFT  removed: ', nft.name)
          j+=1
          self.collection.remove(nft)
    print('Removed ', j, ' NFTs with unwanted attribute combinations.')
  
  def removeNFT_by_name(self, name):
    j=0
    for nft in self.collection:
      for exclusion in name:
        if exclusion==nft.metaData['name']:
          print('NFT  removed: ', nft.name)
          j+=1
          self.collection.remove(nft)  
    print('Removed ', j, ' additional NFTs by metadata specifications.')
          
  def save(self):
    for i in range(0, len(self.collection)):
      name=self.collection[i].image
      x=name.split('.')
      shutil.copyfile('./Inputs/'+name, "./Outputs/"+str(i)+'.'+x[1])
      self.collection[i].renumber(i)
      f=open('./Outputs/'+str(i)+'.json', 'w')
      f.write(json.dumps(self.collection[i].metaData, indent=4))
      f.close()
      
    print('NFTs re-numbered, outputs saved')
      

