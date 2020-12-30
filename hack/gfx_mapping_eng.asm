norom

; NOTES:
; STATUS MENU LAYOUT: 0x393F0 to 0x3947A SNES

; Use 0xFF for empty tile

; NEW GAME SCREEN - END
; Change last byte

org $1ACF9 ; 3ACF9 SNES
    db $05,$75,$47 ; E
	db $05,$75,$48 ; N
	db $05,$75,$49 ; D

; ALL MENUS - LEVEL
org $1B7B2 ; 3B7B2 SNES
    db $CD,$CE,$CF,$CE,$CD


; STATUS - ELEMENTAL/SPECIAL DEFENSE

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
