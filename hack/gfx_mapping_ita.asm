norom

; NOTES:
; STATUS MENU LAYOUT: 0x393F0 to 0x3947A SNES

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
    db $FF,$E8,$E9,$EA,$EB ; DIFESA
    db $02
    db $F0,$F1,$F2,$F3,$F4,$F5 ; ELEMENTALE
    db $02,$FF
    db $E8,$E9,$EA,$EB ; DIFESA
    db $02,$FF
    db $EC,$ED,$EE,$EF ; SPECIALE
    db $00

;;
;; MENU - WEAPONS
;;
org $19977
    ; WEAPONS LEFT ... ... ... ...
    db $DE,$DF,$FF,$E6,$E7,$FF,$D8,$D8,$D8,$D8,$D8,$FF
    
;;
;; MENU - WHITE/BLACK/WIZARD/MAGIC LEFT
;; 0x0397EF

;; 2d b8 10 0f9010 0509 ff 6b98 00
;;
;; 2d 38 10 0c5f01 00 0f5f01 05 8f 80 98 13 14
;; 11 5e 00 05 8a 0f 5f 01 13 04 11 5f 01 14 fc 0b
;; 0c 92 98 21 21 21 21 0a 6f 98 0f 5f 01 0b 0f a4
;; 98 05 47 0b 11 5f 01 02 01 0a 72 98 00
;; ff 0f1810 08ef97
;; ff 0f1910 08ef97
;; ff 0f1a10 08ef97
;; 2880 dcdddedf 2800 0f9010 0b
;; ff de
;;
;; 98
;;
;; --0x0398C9--
;; ff 0f9810 08ef97
;; ff 0f9910 08ef97
;; ff 0f9a10 08ef97 01 08ed98
;; ff dedf 0f9010 0b
;; ff 05
;;
;; --0x0398ED--
;; 2880 d0d1d2d3 2800
;; 2880 d4d5d6d7 2800
;; 2880 d8d9dadb 2800
;; 00

org $198BC ; MAGIC
    db $DA,$DB,$DC,$DD
org $198E3 ; LEFT
    db $DE,$DF
org $198EF ; WHITE
    db $D0,$D1,$D2,$D3
org $198F7 ; BLACK
    db $D4,$D5,$D6,$D7
org $198FF ; WIZARD
    db $FF,$D8,$D9,$FF

;; TEST INVERSIONE QTA. MAGIA
;org $198BA
;   db $FF,$DE,$DF
;   db $0F,$90,$10
;   db $0B
;   db $FF,$D8
;   db $98
;   db $ff,$0f,$98,$10,$08,$ef,$97
;   db $ff,$0f,$99,$10,$08,$ef,$97
;   db $ff,$0f,$9a,$10,$08,$ef,$97,$01,$08,$ed,$98
;   db $28,$80
;   db $dc,$dd,$de,$df
;   db $28,$00
;   db $0f,$90,$10,$0b
;   db $ff,$05


;;
;; MENU - CUSTOMIZE - FAST/SLOW
;;
org $19DA9
    db $E0,$E1 ; FAST
    db $08,$F7,$FF ; JUMP TO FFFFFFFFFFFFFFFFFF00

org $19DAE
    db $E4,$E5 ; SLOW

org $1FFF7
    db $E2,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$E3
    ; This should be 00 terminated but by sheer luck, once
    ; the ROM is in RAM the byte at offset 0x40000 is 00

;;
;; NEW GAME SCREEN - END
;; Change last byte
;;c
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
    db $CB,$CC,$CD,$CE,$CF
    ; db $28,$00
