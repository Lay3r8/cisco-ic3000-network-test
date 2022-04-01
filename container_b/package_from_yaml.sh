echo "Removing old files..."
rm package.tar && rm rootfs.tar

echo "Building docker image..."
docker build -t container_b .

echo "Save docker image to rootfs.tar"
docker save -o rootfs.tar container_b

echo "Packaging..."
ioxclient package .
