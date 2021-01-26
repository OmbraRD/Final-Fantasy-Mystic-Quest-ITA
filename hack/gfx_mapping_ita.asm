arch 65816
lorom

; NOTES:
; STATUS MENU LAYOUT: 0x393F0 to 0x3947A SNES

;;
;; STATUS - ELEMENTAL/SPECIAL DEFENSE
;;

; WINDOW
org $039449
    db $24 ; WINDOW OPCODE
    db $0B ; X POSITION
    db $11 ; Y POSITION
    db $0A ; HEIGHT
    db $09 ; WIDTH
    db $15,$0D ; CONTENT POSITION
    
; POINTER
org $039452
    db $08,$26,$9D

; TILES
org $039D26
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
org $039977
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

org $0398BC ; MAGIC
    db $DA,$DB,$DC,$DD
org $0398E3 ; LEFT
    db $DE,$DF
org $0398EF ; WHITE
    db $D0,$D1,$D2,$D3
org $0398F7 ; BLACK
    db $D4,$D5,$D6,$D7
org $0398FF ; WIZARD
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
org $039DA9
    db $E0,$E1 ; FAST
    db $08,$F7,$FF ; JUMP TO FFFFFFFFFFFFFFFFFF00

org $039DAE
    db $E4,$E5 ; SLOW

org $03FFF7
    db $E2,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$E3
    ; This should be 00 terminated but by sheer luck, once
    ; the ROM is in RAM the byte at offset 0x40000 is 00

;;
;; NEW GAME SCREEN - END
;; Change last byte
;;c
org $03ACF9
    db $05,$75,$47 ; E
    db $05,$75,$48 ; N
    db $05,$75,$49 ; D

;;
;; BATTLE - AUTO/MANUAL
;;
org $03B721
    ; db $28,$80
    db $BA,$BB ; AUTO
    ; db $28,$00

org $03B72A
    ; db $28,$80
    db $BC,$BD,$BE ; MANUAL
    ; db $28,$00

;;
;; ALL MENUS - LEVEL
;;
org $03B7B2 ; 3B7B2 SNES
    ; db $28,$80
    db $CB,$CC,$CD,$CE,$CF
    ; db $28,$00


;;
;; BATTLE - SPELL SUBMENU - BLACK/WHITE/WIZARD MAGIC LEFT
;;

org $3a313
    db $ff,$d8,$d9,$ff

;org $3A2E1
;    db $05,$dc,$03 ; OPCODE 2 BYTES, AMOUNT OF ARGS
;    db $a31a ; POINTER TO WHITE
;    db $a328 ; POINTER TO BLACK
;    db $a30c ; POINTER TO WIZARD
;
;org $3A2EA
;    ;
;    db $28,$80
;    db $dc,$dd,$de,$df ; MAGIC
;    db $28,$00
;    db $de,$df,$ff ; LEFT
;    db $05,$22
;    db $08,$df,$81 ; POINTER?
;    db $08,$ec,$a1 ; POINTER?
;    db $05,$8d,$0f
;    db $02
;    db $00
;    db $05,$4d,$18,$13,$70
;    db $09,$9f,$d2,$00
;    db $00
;
;org $3A30C
;    db $05,$f4,$5f,$01,$1a0
;    db $28,$80
;    db $d8,$d9,$da,$db ; WIZARD
;    db $28,$00
;    db $00
;
;org $3A31A
;    db $05,$f4,$5f,$01,$18
;    db $28,$80
;    db $d0,$d1,$d2,$d3 ; WHITE
;    db $28,$00
;    db $00
;
;org $3A328
;    db $05,$f4,$5f,$01,$19
;    db $28,$80
;    db $d4,$d5,$d6,$d7 ; BLACK
;    db $28,$00
;    db $00
;
;warnpc $3A336