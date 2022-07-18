import axios from "axios"
import { useState } from "react"
import Results from "../components/Results"
import SearchBar from "../components/SearchBar"
import TopBar from "../components/TopBar"

const Home = () => {
  const [query, setQuery] = useState("")
  const [results, setResults] = useState({})
  const [time, setTime] = useState("")

  const search = async (e) => {
    e.preventDefault()

    if (query === "") {
      alert("Enter a query first")
      return
    }

    const data = (
      await axios.post("http://localhost:5000/", {
        query: query,
      })
    ).data

    setResults(data.results)
    setTime(data.time)
  }

  const handleChange = (e) => {
    setQuery(e.target.value)
  }

  return (
    <>
      <TopBar>
        <SearchBar
          value={query}
          handleClick={search}
          handleChange={handleChange}
        />
      </TopBar>
      <div className="flex flex-col mx-[25%]">
        <Results results={results} time={time} />
      </div>
    </>
  )
}

export default Home
