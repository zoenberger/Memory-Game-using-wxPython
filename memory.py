#Basic Memory Game
#All images should be in folder named "Images"
#Images used are W:100px H:150px, though any size works if all images same size
#Line 32 has some commented out code to print the key to terminal for testing.


import wx, os, random, time

class MemoryGame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Memory')
        self.SetSize((900,700))
        self.Move((50,25))
        self.panel = wx.Panel(self)   
        
        
        #define how big game is...can be useful for making skill options later
        self.numPairs = 12
        
     
        #get all images in directory called "Images" & shuffle order
        self.imageArray = GetJpgList("./Images")
        random.shuffle(self.imageArray)
        
        #create array with how many cards needed and double it to make matched pairs        
        self.imagePairs = self.imageArray[0:self.numPairs]
        self.imagePairs = self.imagePairs * 2

        #because we doubled, we need to re-shuffle order
        random.shuffle(self.imagePairs)
        
        #PRINT KEY TO TERMINAL SO YOU CAN QUICKLY SOLVE
#         countrow=0
#         for card in self.imagePairs:
#             countrow +=1
#             if countrow%6 == 0:
#                 print card
#             else:
#                 print card,
        
        #create blank card and give name of file name
        card = wx.Image('card.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.blankCards =[]
        for i in range(len(self.imagePairs)):
            self.blankCards.append(wx.StaticBitmap(self.panel,wx.ID_ANY, card,name=self.imagePairs[i]))
            
        #bind left click to each card that calls check function
        for img in self.blankCards:
            img.Bind(wx.EVT_LEFT_DOWN, self.onClick)
            
      
        #Visual Layout
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        gs = wx.GridSizer(4, 6, 15, 15)
        gs.AddMany(self.blankCards)       
        vbox.Add(gs, proportion=0, flag = wx.LEFT | wx.TOP, border = 10)

        self.panel.SetSizer(vbox)
        self.Show()
        
        self.foundMatches= 0 #Keeps track to see if you've won.
        self.clickCount = 0 #keeps track of 1st or second click.
        self.card1 = '' #holding spot if it's first click

    #----------------------------------------------------------------------
    def onClick(self, event):
        self.clickCount += 1
        
        #get card clicked on, swap out blank image with image by filename
        newCard = event.GetEventObject()
        img = wx.Image(newCard.GetName(), wx.BITMAP_TYPE_ANY)
        newCard.SetBitmap(wx.BitmapFromImage(img))        
        
        if self.clickCount == 1:
            self.card1 = newCard #put into holding space if 1st click
        
        else:
            #FOUND MATCH: Unbind click events. Update match tracker
            if (newCard.GetName() == self.card1.GetName()):
                for findItem in self.blankCards:
                    if findItem.GetName() == newCard.GetName():
                        findItem.Unbind(wx.EVT_LEFT_DOWN)
                self.foundMatches += 1
            else:  
                #NO MATCH: Wait then hide both cards again.              
                time.sleep(1.5) #This basically freezes screen, but clicks still captured.
                blankCard = wx.Image('card.jpg', wx.BITMAP_TYPE_ANY)
                newCard.SetBitmap(wx.BitmapFromImage(blankCard))
                self.card1.SetBitmap(wx.BitmapFromImage(blankCard))
            self.clickCount = 0
        
        if self.foundMatches == self.numPairs:
            Winner()
            
          
#NOTE: Make the winning more exciting. Hahahaha
def Winner():
    print "WINNER WINNER WINNER!"


#get all JPEGs in a directory that is passed and return image names array
#Note I found this code snippet here:   http://wiki.wxpython.org/wxStaticBitmap
def GetJpgList(loc):
    jpgs = [f for f in os.listdir(loc) if f[-4:] == ".jpg"]
    #print "JPGS are:", jpgs
    return [os.path.join(loc, f) for f in jpgs]
      
    
if __name__ == '__main__':
    app = wx.App(False)
    frame = MemoryGame()
    app.MainLoop()