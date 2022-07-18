import Result from "../components/Result"

const Results = ({ results, time }) => {
  if (Object.keys(results).length === 0) {
    if (time === "") {
      return <div className="flex flex-col items-center"></div>
    } else {
      return (
        <div className="flex flex-col items-center">
          <span>
            About {results.length} results ({parseFloat(time).toFixed(3)}{" "}
            seconds)
          </span>
        </div>
      )
    }
  }

  return (
    <div className="flex flex-col items-center">
      <span>
        About {results.length} results ({parseFloat(time).toFixed(3)} seconds)
      </span>
      {results.map((result, index) => {
        return (
          <Result title={result.title} summary={result.summary} key={index} />
        )
      })}
    </div>
  )
}

export default Results
