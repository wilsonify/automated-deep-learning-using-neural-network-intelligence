FROM adl-nni-builder:latest
ENV PATH=/root/.local/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/bin:/usr/sbin
COPY . /book
EXPOSE 8080
ENTRYPOINT ["nvidia-smi"]