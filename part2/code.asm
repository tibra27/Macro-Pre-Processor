!!!M_START ..fun.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
			<*you are in comment*>
			extern printf
			extern atoi
!!!M_FINISH

!!!M_START ..function.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
		WHILE..(&a1& L &a2&)
			mov ecx,&a5&
			INCR &a1&
		ENDW..

!!!M_FINISH

!!!M_START ..condition.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
			IF..(&a2& L &a4&)
				iteration:
					mov ebx,[n]
					cmp ebx,1
					je end
					add eax,ecx
					mov ecx,eax
					push eax
					push int
					call &a6&
					jmp iteration
			ELSE..
				end:
					mov esp,ebp
	                pop ebp
					ret
			END_IFF
!!!M_FINISH

!!!M_STARTS ..macro1.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1) int: db '%d',&a1&,&a2& !!!M_FINISHS

..fun.. ()

SECTION .data
	..macro1.. (10,0)

SECTION .bss
	i RESB 32
	n RESB 32
	S RESB 32

SECTION .text
	global main
main:
	push ebp
	mov ebp,esp
	mov ebx,dword[esp+12]
	mov ecx,[ebx+4]
	push ecx
	call atoi
	mov [n],eax

	mov eax,1
	mov [i],eax

	..function.. (0,4,0,0,0,2,3)

	mov eax,0
	mov [S],eax
	push eax
	push int
	call printf
	add esp,8
	mov ecx,1
..condition.. (1,6,3,4,5,6,7)

