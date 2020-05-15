(format t "Enter positive number~%")
(defvar n (read))
(setq prod 1)
;(setq i 1)
(defun fact(n)
	(if (< n 0)
		(format t "Factorial of negative number doesn't exist~%")
  		(progn
  			(loop for i from 1 to n
      				do (setf prod (* prod i))
  			)
  			(format t "Factorial of given number = ~d" prod)
  		)
	)
)
(fact n)

