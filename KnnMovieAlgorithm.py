{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "38084bbf-4b97-4c36-a902-88ad3ab5aa7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'anime.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/5r/th3v2jl16lv56r3q1c0pg7nw0000gr/T/ipykernel_62775/1827053545.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     43\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mneighbors\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m \u001b[0mfind_neighbors\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0manime_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     46\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mpredict_movies\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmovies\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtest_movie\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mk_neighbors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/var/folders/5r/th3v2jl16lv56r3q1c0pg7nw0000gr/T/ipykernel_62775/1827053545.py\u001b[0m in \u001b[0;36mfind_neighbors\u001b[0;34m(test_movie, k_neighbors)\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfind_neighbors\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_movie\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mk_neighbors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m     \u001b[0mdistances\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 32\u001b[0;31m     \u001b[0mmovies\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mload_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"anime.csv\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     33\u001b[0m     \u001b[0mi\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mmovie\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmovies\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/var/folders/5r/th3v2jl16lv56r3q1c0pg7nw0000gr/T/ipykernel_62775/1827053545.py\u001b[0m in \u001b[0;36mload_csv\u001b[0;34m(filename)\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mload_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0mdataset\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m     \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'r'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mfile\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m         \u001b[0mcsv_reader\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mreader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfile\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcsv_reader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'anime.csv'"
     ]
    }
   ],
   "source": [
    "from math import sqrt\n",
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from csv import reader\n",
    "\n",
    "\n",
    "def load_csv(filename):\n",
    "    dataset = list()\n",
    "    with open(filename, 'r') as file:\n",
    "        csv_reader = reader(file)\n",
    "        for row in csv_reader:\n",
    "            if not row:\n",
    "                continue\n",
    "            dataset.append(row)\n",
    "    return dataset\n",
    "\n",
    "anime_data = load_csv(\"anime.csv\")\n",
    "print(anime_data)\n",
    "\n",
    "def calc_euclidean_distance(movie_1, movie_2):\n",
    "    genre_distance = 0.0\n",
    "    rating_distance = 0.0\n",
    "    members_distance = 0.0\n",
    "    \n",
    "    for x in range(0,43,3):\n",
    "        if (isinstance(movie_1[6][x], int) and isinstance(movie_2[6][x], int)):\n",
    "            genre_distance += (int(movie_1[6][x]) - int(movie_2[6][x]))**2    \n",
    "    if (([not s or s.isspace() for s in movie_1[5]]) and ([not sp or sp.isspace() for sp in movie_2[5]])):\n",
    "        rating_distance += (float(movie_1[5]) - float(movie_2[5]))**2\n",
    "    if (isinstance(movie_1[7], int) and isinstance(movie_2[7], int)):\n",
    "        members_distance = int(movie_1[7]) + int(movie_2[7])\n",
    "        \n",
    "    total_distance = rating_distance + genre_distance + members_distance\n",
    "    return sqrt(total_distance)\n",
    "    \n",
    "def find_neighbors(test_movie, k_neighbors):\n",
    "    distances = list()\n",
    "    movies = load_csv(\"anime.csv\")\n",
    "    i = 1\n",
    "    for movie in range(len(movies)):\n",
    "        calculated_distance = calc_euclidean_distance(test_movie, movie[i])\n",
    "        distances.append((movie[i][1], calculated_distance))\n",
    "        i+=1\n",
    "    distances.sort(key=lambda tup: tup[1])\n",
    "    neighbors = list()\n",
    "    for i in range(k_neighbors):\n",
    "        neighbors.append(distances[i][0])\n",
    "    print(neighbors)\n",
    "    return neighbors\n",
    "\n",
    "find_neighbors(anime_data[2], 5)\n",
    "\n",
    "def predict_movies(movies, test_movie, k_neighbors):\n",
    "    number = 1\n",
    "    neighbors = find_neighbors(movies, test_movie, k_neighbors)\n",
    "    for movie in neighbors:\n",
    "        print ('%d. %d' % (number, movie))\n",
    "        number += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "556b856d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f56e4ea9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}