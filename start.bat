mkdir maps

curl -o SuperMarioBros.py https://raw.githubusercontent.com/nils865/SuperMarioBros.py/main/SuperMarioBros.py
curl -o nilsLib.py https://raw.githubusercontent.com/nils865/nilsLib.py/main/nilsLib.py
curl -o maps/1-1.json https://raw.githubusercontent.com/nils865/SuperMarioBros.py/main/maps/1-1.json
curl -o maps/1-1-sub.json https://raw.githubusercontent.com/nils865/SuperMarioBros.py/main/maps/1-1-sub.json

python SuperMarioBros.py

exit