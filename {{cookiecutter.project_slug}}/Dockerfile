FROM pandoc/extra:latest

RUN apk add --no-cache \
    bash \
    curl \
    tar \
    xz \
    perl \
    fontconfig \
    ttf-dejavu && \
    curl -sSL https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | tar -xz && \
    cd install-tl-* && \
    echo "selected_scheme scheme-basic" > texlive.profile && \
    ./install-tl --profile=texlive.profile && \
    cd .. && rm -rf install-tl-* && \
    tlmgr update --self && \
    tlmgr install pdfpages collection-latexextra && \
    rm -rf /tmp/* /var/tmp/*
