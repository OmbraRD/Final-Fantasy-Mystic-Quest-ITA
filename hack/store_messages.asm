arch 65816
lorom

;;
;; REMOVE "s" AND "et" AT THE END OF OBJECTS
;;
org $3FE7D
    db $0F,$00,$15
    db $08,$83,$83
    db $05,$0B,$FC
    db $88,$FE ; POINTER TO NEXT PHRASE
    ; db $C6 ; s
    db $05,$0B,$FA
    db $8D,$FE
    ; db $B8,$C7 ; et
    db $00,$05

;;
;; REMOVE "s." AT THE END OF CAN'T CARRY ANYMORE
;;
org $3B613
    ;db $C6,$D2 ; s.
    db $D2 ; .
    db $0A,$23,$B6
    ; ADDED
    db $00

org $3b575
    ;db $c6,$ce ; s!
    db $ce ; !
    db $02
    db $10,$b6,$00,$05,$42,$1c,$00
    db $12,$b6,$00,$0c,$b8,$00,$05,$8c,$0c,$6c,$00
    db $13,$0f,$66,$01,$05,$6d,$10,$6c,$00
    db $05,$48,$10,$10,$05,$18,$9e,$00,$02,$51,$00
    db $00 ; ADDED
    db $02