@echo off
REM Geração de um par de chaves pública/privada usando OpenSSL
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private_key.pem -out public_key.pem

REM Geração de um certificado digital autoassinado
openssl req -new -x509 -key private_key.pem -out certificate.pem -days 365 -subj "/CN=Dispositivo IoT"
