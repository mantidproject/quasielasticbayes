SUBROUTINE four(DATA,N,NDIM,ISIGN,IFORM, y_out)
INCLUDE 'mod_data.f90'
INCLUDE 'mod_files.f90'
INCLUDE 'options.f90'

INTEGER N(1), ISIGN, NDIM, IFORM
COMPLEX DATA(4098), y_out(4098)
REAL x_in(m_d), y_in(m_d), e_in(m_d)
!f2py intent(in) :: DATA, N, ISIGN, NDIM, IFORM
!f2py intent(out) :: y_out                               !real parameters
y_out = DATA
call FOUR2(y_out,N,NDIM,ISIGN,IFORM)
RETURN
END SUBROUTINE
