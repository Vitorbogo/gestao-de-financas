import { styled } from '@stitches/react'

export const Table = styled('table', {
  borderCollapse: 'collapse',
  width: '100%',
})

export const TableHeader = styled('th', {
  background: '#F8FAFC',
  borderBottom: '1px solid #E2E8F0',
  boxShadow: '0px 1px 2px rgba(16, 24, 40, 0.05)',
  padding: '20px',
  textAlign: 'left',
})

export const TableRow = styled('tr', {
  borderBottom: '1px solid #E2E8F0',
})

export const TableCell = styled('td', {
  padding: '20px',
})
