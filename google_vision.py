# script to utilize google vision api and grab labels from an image
# the idea is to send an image of a leaf of a tree to google and google will identity the species with a label

def google_vision():
    import io
    import os
    from google.cloud import vision
    from google.cloud.vision import types
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    image_path = 'android_file_path/image.jpg' # to implement: image_file should be set to the path of the selected image in the android app
    file_name = os.path.join(
        os.path.dirname(__file__),
        image_path)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
        if str(label.description) == 'database.entry': # to implement: match the label from the picture with labels from the database
            print('success')
            # to implement: 1. inform the user in the android app of the match 
            # 2. count it in the database entry e.g. database.entry.increment_count()


if __name__ == '__main__':
    google_vision()
