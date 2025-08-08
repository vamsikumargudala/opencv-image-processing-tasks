{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c7d10ba4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import the required Libraries \n",
    "import numpy as np\n",
    "import cv2 as cv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5ea58000",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n    1. creating a Python3 program to draw rectangle and emoji\\n    2. Using RGB and unsigned int datatype\\n'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Target : Create image using python code(numpy and openCV)\n",
    "\n",
    "'''\n",
    "    1. creating a Python3 program to draw rectangle and emoji\n",
    "    2. Using RGB and unsigned int datatype\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9502f061",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating a Rectangle\n",
    "# creating an emoji"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a9f1ad3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "photo = np.zeros((512, 512, 3), dtype = \"uint8\")\n",
    "photo[:] = [255, 255, 255]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7bd81319",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]],\n",
       "\n",
       "       [[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]],\n",
       "\n",
       "       [[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]],\n",
       "\n",
       "       [[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]],\n",
       "\n",
       "       [[255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        ...,\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255],\n",
       "        [255, 255, 255]]], dtype=uint8)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv.rectangle(photo, (500, 500),(500,500), (255,0,255), -1)\n",
    "cv.circle(photo, (256, 256), radius=100, color=[0, 0, 0], thickness=2)\n",
    "# Eyes\n",
    "cv.circle(photo, (220, 220), radius=10, color=[0, 0, 0], thickness=-1)\n",
    "cv.circle(photo, (286, 220), radius=10, color=[0, 0, 0], thickness=-1)\n",
    "# Nose\n",
    "cv.circle(photo, (253, 270), radius=8, color=[0, 0, 0], thickness=-1)\n",
    "cv.line(photo, (245, 270), (253, 245), [0, 0, 0], 2)\n",
    "cv.line(photo, (261, 270), (253, 245), [0, 0, 0], 2)\n",
    "# Mouth\n",
    "cv.ellipse(photo,(256,290),(60,30),0,0,180,0,-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "845ad1fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# To save the file\n",
    "cv.imwrite(\"emoji.jpg\", photo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d6b4cdf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#To  view the image  \n",
    "\n",
    "cv.imshow('red', photo)\n",
    "# Allows us to see image\n",
    "# untill closed forcefully\n",
    "cv.waitKey(10000) \n",
    "\n",
    "cv.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "033dd691",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4049ab77",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
