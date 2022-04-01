echo "Removing old files..."
rm package.tar && rm package.yaml

echo "Building docker image..."
docker build -t container_a .

echo "Generating package.tar..."
ioxclient docker package container_a .

echo "Done!"
