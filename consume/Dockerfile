#FROM gcc:latest as builder
FROM ubuntu:xenial as builder

# Get g++ for compiling, wget to download Boost, git to clone source code repo,
# and make to automate program compilation with Makefile provided
RUN apt-get update \
  && apt-get install -y git \
                        g++ \
                        make \
                        cmake \
                        openssl \
                        libssl-dev \
                        libblkid-dev e2fslibs-dev libboost-all-dev libaudit-dev \
                        wget

RUN \
	rm -rf rabbitmq-c && \
	git clone https://github.com/alanxz/rabbitmq-c.git && \
	cd rabbitmq-c && \
	git checkout -b v0.8.0 && \
	mkdir -p build && \
	cd build && cmake .. && \
	cmake --build . && \
	cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. && \
	make && make install && \
	cd / && rm -rf rabbitmq-c

RUN \
  rm -rf SimpleAmqpClient && \
  git clone https://github.com/alanxz/SimpleAmqpClient.git && \
  cd SimpleAmqpClient && \
  mkdir -p simpleamqpclient-build2 && \
  cd simpleamqpclient-build2 && cmake .. && \
  cmake --build . && \
  cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=/usr/local .. && \
  make && make install && \
  cd / && rm -rf SimpleAmqpClient

COPY . /app
WORKDIR /app
RUN g++ -W -Wall -Wextra -pedantic -std=c++11 -o result -static main.cpp -lSimpleAmqpClient -lrabbitmq -lboost_chrono -lboost_system -lrt -lssl -lcrypto -ldl -lpthread


FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/result ./result
CMD ["/app/result"]