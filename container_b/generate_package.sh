echo "Removing old files..."
rm package.tar && rm package.yaml

echo "Building docker image..."
docker build -t container_b .

echo "Generating package.tar..."
ioxclient docker package container_b .

echo "Done!"
