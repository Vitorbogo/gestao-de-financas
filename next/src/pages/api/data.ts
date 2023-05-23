import axios, { AxiosResponse } from 'axios'
import { NextApiRequest, NextApiResponse } from 'next'

type ApiResponse = {
  message: string
  data: any
}

const fetchData = async (
  req: NextApiRequest,
  res: NextApiResponse<ApiResponse>
) => {
  try {
    const response: AxiosResponse = await axios.get(
      'http://localhost:8000/end-point'
    )
    const data = response.data
    res.status(200).json({ message: 'Success', data })
  } catch (error) {
    console.error(error)
    res.status(500).json({ message: 'Internal Server Error', data: null })
  }
}

export default fetchData
