{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "89490ba1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ca573e8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "03e25d72",
   "metadata": {},
   "outputs": [],
   "source": [
    "img=cv2.imread(\"nature2.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "345ebbbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "img1 = cv2.imread(\"nature.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e3540ed7",
   "metadata": {},
   "outputs": [],
   "source": [
    "img2 = cv2.imread(\"nature2.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0374810e",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('Hello',img1)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dc79fe53",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('Hi',img2)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7c47ff92",
   "metadata": {},
   "outputs": [],
   "source": [
    "cimg1 = img1[100:250,200:500]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c9113cc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "img[100:250,200:500]=cimg1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c13ee672",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('Hello',img)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "04d8ae43",
   "metadata": {},
   "outputs": [],
   "source": [
    "cimg=img2[100:250,100:500]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ed06c9bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "img1[100:250,100:500]=cimg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2d3405c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('Hi',img1)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c1ab756",
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
