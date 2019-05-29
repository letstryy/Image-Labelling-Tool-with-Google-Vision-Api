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
- Move to previous image
  - Click the blue previous Arrow button 
- Move to next image
  - Click the blue next Arrow button
- ZoomIn and ZoomOut
  - Click on the blue ZoomIn and Zoomout button
- Discard the image
  - Click on the blue Discard button
- Output File
  - At the top level of the directory where the program was run, there should be a file called out.csv that contains the generate data
## How to Run

1. Install flask

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
