;;;;
;; Expand ROM to 1MB.
;;
norom

;; Signal 8Mbit.
org $7FD7
    db $0A

;; Fill with zeroes till 1MB.
!address = $80000
while !address < $100000
    org !address
        fillbyte $00 : fill $10000
    !address #= !address+$10000
endif