# Image-Labelling-Tool-with-Google-Vision-Api

A web based tool to label images. It uses Google Vision API returned Bounding Boxes coordinates.

## Features

It runs directly from the browser and bounding boxes on image are clickable and label gets popped up upon clicking the bouding box boundary

- Add a label for a box
  - For the box you would like to give a label, find its id (noted in the top left corner of the box)
- Find the label with the corresponding number
  - Enter the name you want in the input field
  - Press enter
- Remove label click the red button on the label you would like to remove
- Move to next image
  - Click the next Arrow button
- ZoomIn and ZoomOut
  - Click on the ZoomIn and Zoomout button
- Rotate image
  - Restore
  - Rotate 180
  - Rotate 90
  - Rotate -90
- Draw Rectangle
  - Manually draw rectangle
- Remove Rectangle
  - Delete the rectangle
- Discard the image
  - Click on the Discard button
- Output File
  - At the top level of the directory where the program was run, there should be a file called out.csv that contains the generated data whch contains the google id, angle(Click on the rotate button to get the right orientation of the image and get the angle accordingly; for future use, want to crop details, get the image orientation, rotate it according to the angle and then crop) and image coordinates.
## How to Run

1. Install flask
```bash
pip install flask 
```

2. Open the terminal and run 

```bash
python3 app.py 
```
3. Open your browser (if it hasn't popped up already) at: http://127.0.0.1:5000/

4. Login credentials:

   #### username: admin

   #### password: admin

## Built with
This application is built upon following technology stack.

- Python
- Flask
- HTML5-canvas
- JS
## Author
Sneha Rawat [sneharawatt@gmail.com]
