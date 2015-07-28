! This program relies on the two files, grid.in and LM_quant. The names
! are hard coded for the time being, also can only use with grid files
! that contain one grid
      
      program maxvort

      implicit none
      character(80) :: ofile
      integer :: nj,nk,nl,j,k,l,jj,kk,ll,ngrid
      integer :: jt,kt,nq
      real(kind=8) :: maxv 
      real(kind=8), dimension(:,:,:), allocatable :: x,y,z,lmvars
      open(1,file='grid.in',status='old',form='unformatted') 
      read(1) ngrid 
      read(1) nj,nk,nl
       
      allocate( x(nj,nk,nl) )
      allocate( y(nj,nk,nl) )
      allocate( z(nj,nk,nl) )

      read(1) (((x(jj,kk,ll),jj=1,nj),kk=1,nk),ll=1,nl),
     &        (((y(jj,kk,ll),jj=1,nj),kk=1,nk),ll=1,nl),
     &        (((z(jj,kk,ll),jj=1,nj),kk=1,nk),ll=1,nl)
      close(1) 
      
      open(2,file='LM_quant',status='old',form='unformatted')
      read(2) jt,kt,nq

      allocate( lmvars(jt,kt,nq) )
      read(2) lmvars 
      close(2) 
 
      ofile = 'MaxRe_v.txt' 
      open(3,file=ofile,status='replace',form='formatted') 
      do j = 1,nj
         maxv = 0.0
         do k = 1,140
            if (lmvars(j,k,1) .gt. maxv) then   
               maxv = lmvars(j,k,1) 
            endif
         enddo
         write(3,*) j,x(j,1,2),maxv 
      enddo    






      end 
