FROM msranni/nni:v2.5
RUN mkdir /book
ADD . /book
EXPOSE 8080
ENTRYPOINT ["tail", "-f", "/dev/null"]