(defvar a '(1 2 3 4))
(format t "Enter the index~%")
(defvar n (read))
(format t "List is : ~a~%" a)
(defun list_element(n)
	(if (or (< n 0) (>= n (list-length a)))
		(format t "List index is not valid~%")
		(progn
		(loop for i from 0 to (- n 1) do
      			(setf a (cdr a))
		)
		(format t "Element at index ~a in list = ~a~%" n (car a))
		)
	)
)
(list_element n)