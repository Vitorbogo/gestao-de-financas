import { styled } from '@stitches/react'

export const SideBar = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  padding: '0px 18px 32px',
  gap: '48px',

  width: '20vw',
  height: '100vh',
  minWidth: '264px',

  background: '#080325',
  boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
})

export const MenuItemsWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  minWidth: '264px',

  flexGrow: 1,
})

export const MenuSettingsWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  padding: '0px',
  background: '#080325',
})

export const LogoWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
  alignItems: 'center',
  padding: '24px 0px',
  gap: '52px',
})

export const MenuItemsContainer = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',

  flexGrow: '0',
})

export const MenuItemWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  padding: '20px',
  gap: '17px',
  width: '264px',
  height: '72px',
  backgroundColor: '#080325',
  borderRadius: '4px',
  flexGrow: 0,

  '&:hover': {
    backgroundColor: '#191A38',
  },
})

export const MenuItemText = styled('span', {
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: 600,
  fontSize: '14px',
  lineHeight: '20px',
  color: '#FFFFFF',
  flex: 'none',
  order: 1,
  flexGrow: 0,
})
