#! /bin./bash

apt-get update
apt-get install -qy apt-transport-https dirmngr
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | tee /etc/apt/sources.list.d/mono-official-vs.list

apt-get update
apt-get install -qy mono-devel nunit nunit-console libnunit-cil-dev
