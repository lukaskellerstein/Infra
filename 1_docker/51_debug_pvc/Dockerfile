FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    util-linux \
    file \
    bsdextrautils \
    less \
    nano \
    vim \
    tree \
    lsof \
    curl \
    wget \
    unzip \
    zip \
    rsync \
    net-tools \
    iputils-ping \
    pciutils \
    procps \
    gnupg \
    jq \
    tmux \
    htop \
    strace \
    gdb \
    binutils \
    parted \
    fdisk \
    kpartx \
    ntfs-3g \
    e2fsprogs \
    dosfstools \
    git \
    qemu-utils \
    xxd \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /mnt/pvc

CMD ["/bin/bash"]
