norom

;;
;; STATUS - ELEMENTAL/SPECIAL DEFENSE
;;

; WINDOW
org $19449
    db $24 ; WINDOW OPCODE
    db $0B ; X POSITION
    db $11 ; Y POSITION
    db $0A ; HEIGHT
    db $09 ; WIDTH
    db $15,$0D ; CONTENT POSITION

; POINTER
org $19452
    db $08,$26,$9D

; TILES
org $19D26 ; 39D26 SNES
    db $F0,$F1,$F2,$F3,$F4,$F5 ; ELEMENTAL
    db $02,$FF
    db $E8,$E9,$EA,$EB ; DEFENSE
    db $02,$FF
    db $EC,$ED,$EE,$EF ; SPECIAL
    db $02,$FF
    db $E8,$E9,$EA,$EB ; DEFENSE
    db $00

;;
;; MENU - WEAPONS - WEAPONS LEFT
;;
org $19977
    ; WEAPONS LEFT ... ... ... ...
    db $E4,$E5,$E6,$E7,$DE,$DF,$FF,$D8,$D8,$D8,$D8,$FF

;;
;; MENU - WHITE/BLACK/WIZARD/MAGIC LEFT

org $198BC ; MAGIC
    db $DC,$DD,$DE,$DF
org $198E3 ; LEFT
    db $DE,$DF
org $198EF ; WHITE
    db $D0,$D1,$D2,$D3
org $198F7 ; BLACK
    db $D4,$D5,$D6,$D7
org $198FF ; WIZARD
    db $D8,$D9,$DA,$DB

;;
;; MENU - CUSTOMIZE
;;
org $19DA9
    db $E0,$E1 ; FAST
    ; db $08,$29,$A4 ; JUMP TO FFFFFFFFFFFFFFFFFF00

org $19DAE
    db $E2,$E3 ; SLOW

;org $1FFF7
    ;db $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF
    ; This should be 00 terminated but by sheer luck, once
    ; the ROM is in RAM the byte at offset 0x40000 is 00

;;
;; NEW GAME SCREEN - END
;; Change last byte
;;
org $1ACF9 ; 3ACF9 SNES
    db $05,$75,$47 ; E
    db $05,$75,$48 ; N
    db $05,$75,$49 ; D

;;
;; BATTLE - AUTO/MANUAL
;;
org $1B721
    ; db $28,$80
    db $BA,$BB ; AUTO
    ; db $28,$00

org $1B72A
    ; db $28,$80
    db $BC,$BD,$BE ; MANUAL
    ; db $28,$00

;;
;; ALL MENUS - LEVEL
;;
org $1B7B2 ; 3B7B2 SNES
    ; db $28,$80
    db $CD,$CE,$CF,$CE,$CD
    ; db $28,$00
