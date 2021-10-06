#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def imageBlur(imageURL):
    "This takes an image URL, blurs the image, and returns a new file"
    from PIL import Image
    inputImage = Image.open(imageURL)
    pixels = inputImage.load()
    lenCol = inputImage.size[0] #width of image, in pixels
    lenRow = inputImage.size[1] #height of image, in pixels
    newImage = Image.new('RGB', (lenCol,lenRow), "black") #create a blank new image to update
    newImagepixels = newImage.load()

    for currentRow in range(0,lenCol):
        for currentCol in range(0,lenRow):
            count = 0
            newR = 0 
            newG = 0
            newB = 0
            for row in range(currentRow-1,currentRow+2): 
                for col in range(currentCol-1, currentCol+2):
                    if((row>-1) and (col>-1) and (row<lenRow) and (col<lenCol)):
                        newR += pixels[row,col][0]
                        newG += pixels[row,col][1]
                        newB += pixels[row,col][2]
                        count+=1
            newImagepixels[currentRow,currentCol] = (round(newR/count),round(newG/count), round(newB/count))
    
    newImageURL = imageURL.split('.')[0]+" (blurred)."+imageURL.split('.')[1]    
    newImage.save(newImageURL)


# In[ ]:


print('Welcome to ImageBlur!')
while True:
    try:
        imageURL = input('Please enter a filepath to your image, e.g. "Documents/image.jpg" (Type 0 to quit):') 
        if(imageURL == '0'):
            break
        print("All right, one blurred image coming right up!")
        imageBlur(imageURL)
        print("Done!")
    except:
        print("Apologies, something has gone wrong. Please check to make sure you're entering the correct filepath.")

