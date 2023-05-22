import { styled } from '@stitches/react'

export const MainWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'flex-end',
  width: '100%',
})

export const MainContainer = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  width: '100%',
  flex: '1',
})

export const TopDiv = styled('div', {
  boxSizing: 'border-box',
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
  alignItems: 'flex-start',
  padding: '36px 48px',
  gap: '664px',

  width: '100%',
  height: '100px',

  background: '#FFFFFF',
  borderBottom: '1px solid #E2E8F0',
  boxShadow:
    '0px 1px 3px rgba(16, 24, 40, 0.1), 0px 1px 2px rgba(16, 24, 40, 0.06)',
})

export const TitleContainer = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  padding: '36px 48px',
  gap: '95px',
  height: '140px',
  backgroundColor: '#FFFFFF',
})

export const TitleDiv = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  gap: '8px',
  width: '383px',
  height: '68px',
})

export const Title = styled('h1', {
  fontFamily: "'Inter'",
  fontStyle: 'normal',
  fontWeight: '700',
  fontSize: '32px',
  lineHeight: '40px',
  color: '#121212',
})

export const SubTitle = styled('h2', {
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: 400,
  fontSize: '14px',
  lineHeight: '20px',
  color: '#5B6776',
})

export const MainContent = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  padding: '0px 48px',
  gap: '24px',
  height: '100%',
  backgroundColor: '#FFFFFF',
  width: '100%',
})

export const FirstRow = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'flex-start',
  margin: '0px 24px 0px 24px',
  gap: '24px',
  border: '1px solid #000',
})

export const WalletInfo = styled('div', {
  boxSizing: 'border-box',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  padding: '16px 24px',
  gap: '21px',
  width: '50%',
  height: '160px',
  backgroundColor: '#FFFFFF',
  border: '1px solid #E2E8F0',
  boxShadow:
    '0px 1px 3px rgba(16, 24, 40, 0.1), 0px 1px 2px rgba(16, 24, 40, 0.06)',
  borderRadius: '6px',
  flex: 'none',
  order: '0',
  flexGrow: '0',
})

export const WalletInfoTitle = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  padding: '0px',
  gap: '16px',
})

export const WalletInfoTitleText = styled('h3', {
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: '700',
  fontSize: '24px',
  lineHeight: '30px',
  color: '#121212',
})

export const BalanceText = styled('h3', {
  width: '572px',
  height: '40px',
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: '400',
  fontSize: '32px',
  lineHeight: '40px',
  letterSpacing: '-0.024em',
  color: '#344055',
})

export const PaymentAction = styled('div', {
  boxSizing: 'border-box',
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
  alignItems: 'flex-start',
  padding: '30px 24px',
  gap: '58px',
  isolation: 'isolate',
  width: '400px',
  height: '160px',
  backgroundColor: '#FFFFFF',
  border: '1px solid #E2E8F0',
  boxShadow:
    '0px 1px 3px rgba(16, 24, 40, 0.1), 0px 1px 2px rgba(16, 24, 40, 0.06)',
  borderRadius: '6px',
  flex: 'none',
  order: '1',
  flexGrow: '1',
})

export const PaymentDiv = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  gap: '10px',
})

export const PaymentContent = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  minWidth: '150px',
  minHeight: '100px',
  gap: '18px',
})

export const PaymentText = styled('h3', {
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: 600,
  fontSize: '16px',
  lineHeight: '20px',
  textAlign: 'center',
  color: '#344055',
})

export const AllWalletWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  gap: '16px',
  width: '1054px',
  height: '340px',
  order: '1',
  margin: '0px 24px 0px 24px',
})

export const WalletCardRow = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'flex-start',
  padding: '0px',
  gap: '16px',
  width: '1044px',
  height: '162px',
  flex: 'none',
  order: '0',
  flexGrow: '0',
})

export const WalletWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  padding: '24px',
  gap: '18px',
  height: '162px',
  background: '#FFFFFF',
  border: '1px solid #E2E8F0',
  boxShadow: '0px 1px 2px rgba(16, 24, 40, 0.05)',
  borderRadius: '6px',
  flexGrow: '1',
})

export const WalletHeader = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  padding: '0px',
  gap: '8px',
  width: '289px',
  height: '58px',
  alignSelf: 'stretch',
})

export const WalletTitleDiv = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  padding: '0px',
  gap: '12px',
  width: '289.33px',
  height: '32px',
  alignSelf: 'stretch',
})

export const WalletDescription = styled('p', {
  fontFamily: 'Inter',
  fontStyle: 'normal',
  fontWeight: '400',
  fontSize: '12px',
  lineHeight: '18px',
  color: '#79808A',
  alignSelf: 'stretch',
})

export const WalletProgressStatusWrapper = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'flex-start',
  gap: '4px',
  width: '289.33px',
  height: '38px',
  alignSelf: 'stretch',
})

export const NewWalletWrapper = styled('div', {
  boxSizing: 'border-box',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  padding: '23px 274px',
  gap: '14px',
  height: '124px',
  background: '#F7F8FD',
  border: '1px solid #E2E8F0',
  boxShadow: '0px 1px 2px rgba(16, 24, 40, 0.05)',
  borderRadius: '6px',
  alignSelf: 'stretch',
})

export const NewWalletIcon = styled('div', {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
  alignItems: 'center',
  padding: '12px',
  gap: '4px',
  width: '40px',
  height: '40px',
  background: '#4F46E5',
  borderRadius: '50%',
  color: '#FFFFFF',
})

export const NewWalletText = styled('p', {
  fontFamily: 'Inter',
  fontWeight: '600',
  fontSize: '18px',
  lineHeight: '24px',
  letterSpacing: '-0.02em',
  color: '#4F46E5',
})
