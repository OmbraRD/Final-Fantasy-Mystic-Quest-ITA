arch 65816
lorom

;; Fill with 0x00
!textstart = $03b7bd
!textend = $03ba35
while !textstart < !textend
    org !textstart
        fillbyte $00 : fill $01
    !textstart #= !textstart+$01
endif


;; TABLE FOR INSERTION
table "credits.tbl",rtl

;;------------------------------------------------------------------------------
;; Credits: 0x3B7BD-0x3BA34
;;------------------------------------------------------------------------------
org $03805f
    dl Start ; $BD,$B7,$03 ; Pointer 0x03b7bd
    dl $7f0000 ; Offset in RAM
    dw End-Start ; Size of data ; $78,$02

org $0380b8
    dw End-Start

; Buffer size
org $ca57e
    cpx #End-Start

;org $ca56a
;    sep #$20
;    ldx #$0000 ; Lower bytes of RAM address
;    lda #$01
;    pea $007f ; Higher byte of RAM address

;org $a1c6
;    lda $0000,y ; Lower bytes of RAM address
;    tax
;    lda $0002,y ; Lower bytes of RAM address
    
; If at the end is reached keep printing empty
; lines until the screen is cleared
org $9ad1
    cmp #End-Start

;org $9adf
;    lda $0000,x

;org $12E000
org $07F900
Start:
    db "Storia",$01
    db "CHIHIRO FUJIOKA",$01
    db $01
    db "Direttore Creativo",$01
    db "KOUZI IDE",$01
    db $01
    db "Design dei Mostri",$01
    db "MASANORI 'JUN' MORITA",$01
    db $01
    db "Design della Mappa",$01
    db "Hideshi Kyohnen",$01
    db $01
    db "Traduzione & Trama",$01
    db "Yoshi Maekawa",$01
    db "Ted Woolsey",$01
    db $01
    db "Programmazione Generale",$01
    db "Katsuhiro Kondoh",$01
    db $01
    db "Programmazione Battaglia",$01
    db "Shingo Tanaka",$01
    db $01
    db "Programmazione Campo",$01
    db "Kiyotaka Goto",$01
    db "Kazuhiko Yoshioka",$01
    db $01
    db "Programmazione Sistema",$01
    db "Itikiti",$01
    db $01
    db "Programmazione Suono",$01
    db "Minoru Akao",$01
    db $01
    db "Grafica della Mappa",$01
    db "PICASSO KABE",$01
    db $01
    db "Grafica dei Mostri",$01
    db "Yuki 'HM' Yasuda",$01
    db $01
    db "Animazione",$01
    db "Toshiyuki Momose",$01
    db $01
    db "Personaggi sulla Mappa",$01
    db "M. Shimoji",$01
    db $01
    db "Compositori",$01
    db "R. Sasai",$01
    db "Y. Kawakami",$01
    db $01
    db "Ringraziamenti Speciali",$01
    db "T. Fujii",$01
    db "Carol Moriyama",$01
    db "Kats A. Tayama",$01
    db "H. Yukitake",$01
    db "K. Adachi",$01
    db "K. Kokubo",$01
    db "H. Minaba",$01
    db "K. Beloit",$01
    db "C. Budd",$01
    db "K. Kreider",$01
    db "K. Kirchner",$01
    db "V. Mayhew",$01
    db "M. Ridley",$01
    db "R. Silveira",$01
    db "H. Suzuki",$01
    db "N. Williams",$01
    db "J. Yanagihara",$01
    db $01
    db "Traduzione Italiana",$01
    db "-- Mumble Translations --",$01
    db "Ombra, Chester, Clomax"
    db $00
End: