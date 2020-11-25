﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.GrpcClients;
using Cityinformation;
using Grpc.Core;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using static Cityinformation.CityService;

namespace Api.Controller
{
    [Route("api/[controller]")]
    [ApiController]
    public class CityController : ControllerBase
    {
        private readonly IGrpcClient _client;

        public CityController(IGrpcClient client)
        {
            _client = client;
        }

        // GET: api/City
        [HttpGet]
        public async Task<IActionResult> Get([FromQuery] SearchRequest request)
        {
            var response = _client.ExecuteAndMerge<SearchRequest, SearchResponse>(request);

            return Ok(await response);
        }

    }
}